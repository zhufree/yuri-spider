import json
import sqlite3

# steam
platform_dict = {
    'chengguang': 11
}

platform = 'chengguang'
db_path = '../yuri-backend/.tmp/data.db'


def get_game_and_id():
    game_dict = {}
    connect = sqlite3.connect(db_path)
    cursor = connect.cursor()
    rows = cursor.execute("SELECT id, gId from games")
    for r in rows:
        # bid = r[1]
        # game_dict[bid] = r[0]
        game_dict[r[1]] = r[0]  # gId: id
    return game_dict



def save_games():
    print('更新game')
    old_game_id_dict = get_game_and_id()
    with open("{}-items.json".format(platform), 'r', encoding='utf-8') as f:
        lines = f.readlines()
        connect = sqlite3.connect(db_path)
        cursor = connect.cursor()
        for line in lines:
            l = json.loads(line)
            sql = ''
            try:
                if l['gId'] in old_game_id_dict.keys():
                    update_data = "intro = '{}', cover = '{}', status = '{}', collectionCount = {}, \
                        up = {}".format(
                        l['intro'].replace("'", '|') if l['intro'] != None else '', 
                        l['cover'], l['status'], 
                        int(l['collectionCount']) if l['collectionCount'] != None else -1)
                    sql = "UPDATE games SET {} WHERE name = '{}'".format(update_data, l['name'])
                    cursor.execute("UPDATE games SET {} WHERE name = '{}'".format(update_data, l['name']))
                else:
                    cursor.execute('''INSERT INTO games (name, url, gId, cover, author, authorUrl, intro, \
                        status, publishTime, collectionCount) VALUES (?,?,?,?,?,?,?,?,?,?)''',
                        (l['name'],l['url'], l['gId'], l['cover'], l['author'], l['authorUrl'],
                        l['intro'], l['status'], l['publishTime'], l['collectionCount']))
            except Exception as e:
                print(sql)
                raise e
            
        connect.commit()
        connect.close()



def get_tag_and_id():
    tag_dict = {}
    connect = sqlite3.connect(db_path)
    cursor = connect.cursor()
    rows = cursor.execute("SELECT id, name from tags")
    for r in rows:
        _id = r[0]
        name = r[1]
        tag_dict[name] = _id
    return tag_dict


def save_tags():
    print('更新tag')
    tag_list = []
    old_tag_list = get_tag_and_id()
    with open("{}-items.json".format(platform), 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            item = json.loads(line)
            tag_list += item['tags']
    tag_list = list(set(tag_list))
    tag_list = [i for i in tag_list if len(i) > 0]
    connect = sqlite3.connect(db_path)
    cursor = connect.cursor()
    for t in tag_list:
        if t not in old_tag_list.keys():
            # insert or ignore exist tags
            cursor.execute('''INSERT OR IGNORE INTO tags (name) VALUES (?)''', (t,))
    connect.commit()
    connect.close()

def add_tags():
    print('添加game和tag关联')
    tag_id_dict = get_tag_and_id() # dict from db
    game_id_dict = get_game_and_id()
    connect = sqlite3.connect(db_path)
    cursor = connect.cursor()
    rows = cursor.execute("SELECT game_id, tag_id from games__tags")
    game_tag_dict = {}
    for r in rows:
        game_id = r[0]
        tag_id = r[1]
        if game_id in game_tag_dict.keys():
            game_tag_dict[game_id].append(tag_id)
        else:
            game_tag_dict[game_id] = [tag_id]
    with open("{}-items.json".format(platform), 'r', encoding='utf-8') as f:
        lines = f.readlines()
        connect = sqlite3.connect(db_path)
        cursor = connect.cursor()
        for line in lines:
            item = json.loads(line)
            game_id = game_id_dict[item['gId']] # insert game by game
            tag_ids = []
            for t in item['tags']: 
                if t in tag_id_dict.keys(): # get all tags for one game
                    tag_ids.append(tag_id_dict[t])
            for tag_id in tag_ids: # insert game-tag relation one by one
                if game_id not in game_tag_dict.keys() or tag_id not in game_tag_dict[game_id]:
                    # check if the tag and game connection exist
                    cursor.execute("INSERT INTO games__tags (game_id, tag_id) \
                    VALUES ({}, {})".format(game_id, tag_id))
        connect.commit()
        connect.close()

if __name__ == '__main__':
    save_games()
    save_tags()
    add_tags()
