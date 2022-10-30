import json
import sqlite3

# 猫耳数据没抓全
platform_dict = {
    'fanjiao': 3,
    'maoer': 4,
    'manbo': 5,
}

platform = 'fanjiao'
db_path = '../yuri-backend/.tmp/data.db'


# 先录入up，再录入drama，匹配up和drama
def save_ups():
    print('更新up')
    up_list = []
    old_up_list = get_up_and_id()
    with open("{}-items.json".format(platform), 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            item = json.loads(line)
            if 'up' in item.keys():
                if item['up'] == '轻之声GL广播剧社':
                    item['up'] = '轻之声广播剧社'
                up_list.append(item['up'])
    up_list = list(set(up_list))
    up_list = [i for i in up_list if len(i) > 0]
    connect = sqlite3.connect(db_path)
    cursor = connect.cursor()
    for u in up_list:
        if u not in old_up_list.keys():
            # insert or ignore exist ups
            cursor.execute('''INSERT OR IGNORE INTO audio_staffs (name, staffType) VALUES (?, ?)''', (u, '["up"]'))
    connect.commit()
    connect.close()


def get_up_and_id():
    up_dict = {}
    connect = sqlite3.connect(db_path)
    cursor = connect.cursor()
    rows = cursor.execute("SELECT id, name from audio_staffs")
    for r in rows:
        _id = r[0]
        name = r[1]
        up_dict[name] = _id
    connect.close()
    return up_dict


def get_drama_and_id():
    drama_dict = {}
    connect = sqlite3.connect(db_path)
    cursor = connect.cursor()
    rows = cursor.execute("SELECT id, fj_id from audio_dramas")
    for r in rows:
        # bid = r[1]
        # drama_dict[bid] = r[0]
        drama_dict[r[1]] = r[0]  # fj_id: id
    connect.close()
    return drama_dict


def play_count_key():
    if platform == 'fanjiao':
        return 'fj_play_count'
    elif platform == 'maoer':
        return 'mr_play_count'
    elif platform == 'manbo':
        return 'mb_play_count'

def get_platform_id():
    if platform == 'fanjiao':
        return 'fj_id'
    elif platform == 'maoer':
        return 'mr_id'
    elif platform == 'manbo':
        return 'mb_id'

def save_dramas():
    print('更新drama')
    up_id_dict = get_up_and_id()
    old_drama_id_dict = get_drama_and_id() # fanjiao only
    connect = sqlite3.connect(db_path)
    cursor = connect.cursor()
    with open("{}-items.json".format(platform), 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
        for line in lines:
            l = json.loads(line)
            if 'up' in l.keys() and l['up'] in up_id_dict.keys():
                up_id = up_id_dict[l['up']]
            else:
                up_id = None
            sql = ''
            try:
                if l['adid'] in old_drama_id_dict.keys():
                    update_data = "intro = '{}', cover = '{}', status = '{}', {} = {}, \
                        {} = {}".format(
                        l['intro'].replace("'", '|') if l['intro'] != None else '', 
                        l['cover'], l['status'], play_count_key(),
                        int(l['playCount']) if l['playCount'] != None else -1, 
                        get_platform_id(), int(l['adid']) if l['adid'] != None else 0)
                    sql = "UPDATE audio_dramas SET {} WHERE {} = '{}'".format(update_data, get_platform_id(), l['adid'])
                    cursor.execute("UPDATE audio_dramas SET {} WHERE {} = '{}'".format(update_data, get_platform_id(), l['adid']))
                    # update up
                    if up_id:
                        cursor.execute(f'UPDATE audio_dramas_up_links SET audio_staff_id = {up_id} WHERE audio_drama_id = {cursor.lastrowid}')
                else:
                    sql = '''INSERT INTO audio_dramas (name, intro, cover, status, {}, {}) VALUES (?,?,?,?,?,?)'''.format(play_count_key(), get_platform_id())
                    cursor.execute(sql, (l['name'], l['intro'], l['cover'], l['status'], l['playCount'], l['adid']))
                    # add audio_drama up link
                    if up_id:
                        cursor.execute('''INSERT OR IGNORE INTO audio_dramas_up_links (audio_drama_id, audio_staff_id) VALUES (?, ?)''', 
                            (cursor.lastrowid, up_id))
            except Exception as e:
                print(sql)
                print(e)
                raise e
            
        connect.commit()
        print('commit')
        connect.close()


def add_platforms():
    print('添加drama和platform关联')
    drama_id_dict = get_drama_and_id()
    connect = sqlite3.connect(db_path)
    cursor = connect.cursor()
    rows = cursor.execute("SELECT audio_drama_id, platform_id from audio_dramas_platforms_links")
    drama_platform_dict = {}
    for r in rows:
        drama_id = r[0]
        platform_id = r[1]
        if drama_id in drama_platform_dict.keys():
            drama_platform_dict[drama_id].append(platform_id)
        else:
            drama_platform_dict[drama_id] = [platform_id]
    with open("{}-items.json".format(platform), 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            item = json.loads(line)
            drama_id = drama_id_dict[item['adid']] # get drama id
            platform_id = platform_dict[platform]
            if drama_id not in drama_platform_dict.keys() or platform_id not in drama_platform_dict[drama_id]:
                # check if the drama and platform connection exist
                cursor.execute("INSERT INTO audio_dramas_platforms_links (audio_drama_id, platform_id) \
                VALUES ({}, {})".format(drama_id, platform_id))
        connect.commit()
        connect.close()


if __name__ == '__main__':
    # clear_data()
    save_ups()
    save_dramas()
    add_platforms()
