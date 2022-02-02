import json
import sqlite3

# 猫耳数据没抓全
platform_dict = {
    'fanjiao': 3,
    'maoer': 4,
    'manbo': 5,
}

platform = 'maoer'
db_path = '../yuri-backend/.tmp/data.db'

# 数据清洗，去重，以最新的为准
def clear_data():
    result_list = []
    name_list = []
    with open("{}-items.json".format(platform), 'r', encoding='utf-8') as f:
        lines = f.readlines()
        lines.sort(key=lambda line: json.loads(line)['adid'])
        lines.reverse()
        for l in lines:
            if json.loads(l)['name'] not in name_list:
                name_list.append(json.loads(l)['name'])
                result_list.append(l)
            else:
                print('already exist, change to newer one')
        print(len(result_list))
    with open("save-{}-items.json".format(platform), 'w', encoding='utf-8') as f:
        f.writelines(result_list)


# 先录入up，再录入drama，匹配up和drama
def save_ups():
    print('更新up')
    up_list = []
    old_up_list = get_up_and_id()
    with open("save-{}-items.json".format(platform), 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            item = json.loads(line)
            if 'up' in item.keys():
                up_list.append(item['up'])
    up_list = list(set(up_list))
    up_list = [i for i in up_list if len(i) > 0]
    connect = sqlite3.connect(db_path)
    cursor = connect.cursor()
    for u in up_list:
        if u not in old_up_list.keys():
            # insert or ignore exist ups
            cursor.execute('''INSERT OR IGNORE INTO ups (name) VALUES (?)''', (u,))
    connect.commit()
    connect.close()


def get_up_and_id():
    up_dict = {}
    connect = sqlite3.connect(db_path)
    cursor = connect.cursor()
    rows = cursor.execute("SELECT id, name from ups")
    for r in rows:
        _id = r[0]
        name = r[1]
        up_dict[name] = _id
    return up_dict


def get_drama_and_id():
    drama_dict = {}
    connect = sqlite3.connect(db_path)
    cursor = connect.cursor()
    rows = cursor.execute("SELECT id, name from audio_dramas")
    for r in rows:
        # bid = r[1]
        # drama_dict[bid] = r[0]
        drama_dict[r[1]] = r[0]  # name: id
    return drama_dict


def play_count_key():
    if platform == 'fanjiao':
        return 'fjPlayCount'
    elif platform == 'maoer':
        return 'mrPlayCount'


def save_dramas():
    print('更新drama')
    up_id_dict = get_up_and_id()
    old_drama_id_dict = get_drama_and_id()
    with open("save-{}-items.json".format(platform), 'r', encoding='utf-8') as f:
        lines = f.readlines()
        connect = sqlite3.connect(db_path)
        cursor = connect.cursor()
        for line in lines:
            l = json.loads(line)
            if 'up' in l.keys() and l['up'] in up_id_dict.keys():
                up_id = up_id_dict[l['up']]
            else:
                up_id = 0

            sql = ''
            try:
                if l['name'] in old_drama_id_dict.keys():
                    update_data = "intro = '{}', cover = '{}', status = '{}', {} = {}, \
                        up = {}".format(
                        l['intro'].replace("'", '|') if l['intro'] != None else '', 
                        l['cover'], l['status'], play_count_key(),
                        int(l['playCount']) if l['playCount'] != None else -1, 
                        up_id)
                    sql = "UPDATE audio_dramas SET {} WHERE name = '{}'".format(update_data, l['name'])
                    cursor.execute("UPDATE audio_dramas SET {} WHERE name = '{}'".format(update_data, l['name']))
                else:
                    cursor.execute('''INSERT INTO audio_dramas (name, intro, cover, status, {}, \
                        up) VALUES (?,?,?,?,?,?)'''.format(play_count_key()),
                        (l['name'], l['intro'], l['cover'], l['status'], l['playCount'], up_id))
            except Exception as e:
                print(sql)
                raise e
            
        connect.commit()
        connect.close()


def add_platforms():
    print('添加drama和platform关联')
    drama_id_dict = get_drama_and_id()
    connect = sqlite3.connect(db_path)
    cursor = connect.cursor()
    rows = cursor.execute("SELECT audio_drama_id, platform_id from audio_dramas__platforms")
    drama_platform_dict = {}
    for r in rows:
        drama_id = r[0]
        platform_id = r[1]
        if drama_id in drama_platform_dict.keys():
            drama_platform_dict[drama_id].append(platform_id)
        else:
            drama_platform_dict[drama_id] = [platform_id]
    with open("save-{}-items.json".format(platform), 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            item = json.loads(line)
            drama_id = drama_id_dict[item['name']] # get drama id
            platform_id = platform_dict[platform]
            if drama_id not in drama_platform_dict.keys() or platform_id not in drama_platform_dict[drama_id]:
                # check if the drama and platform connection exist
                cursor.execute("INSERT INTO audio_dramas__platforms (audio_drama_id, platform_id) \
                VALUES ({}, {})".format(drama_id, platform_id))
        connect.commit()
        connect.close()


if __name__ == '__main__':
    clear_data()
    save_ups()
    save_dramas()
    add_platforms()
