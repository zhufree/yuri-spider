import json
import sqlite3

# 猫耳数据没抓全
platform_dict = {
    'fanjiao': 3,
    'maoer': 4,
    'manbo': 5,
}

db_path = '../yuri-backend/.tmp/data.db'

# 猫耳的数据需要，数据清洗，去重，以最新的为准
def clear_data(platform):
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
    with open("{}-items.json".format(platform), 'w', encoding='utf-8') as f:
        f.writelines(result_list)

# 先录入up，再录入drama，匹配up和drama
def save_ups(platform):
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
                if item['up'] == '桂圆翊宝':
                    item['up'] = '桂圆翊宝（张宇琦）'
            if item['up'] != '' and item['up'] != None:
                up_list.append(item['up'])
    up_list = list(set(up_list))
    up_list = [i for i in up_list if len(i) > 0]
    connect = sqlite3.connect(db_path)
    cursor = connect.cursor()
    for u in up_list:
        if u not in old_up_list.keys():
            # insert or ignore exist ups
            cursor.execute('''INSERT OR IGNORE INTO audio_staffs (name, staff_type) VALUES (?, ?)''', (u, '["up"]'))
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
    return up_dict


def get_drama_platform_id_and_id(platform):
    drama_dict = {}
    connect = sqlite3.connect(db_path)
    cursor = connect.cursor()
    rows = cursor.execute(f"SELECT id, {get_platform_id(platform)} from audio_dramas where {get_platform_id(platform)} IS NOT NULL")
    for r in rows:
        # bid = r[1]
        # drama_dict[bid] = r[0]
        drama_dict[r[1]] = r[0]  # platform_id/adid: id
    return drama_dict

def get_drama_name_and_id():
    drama_dict = {}
    connect = sqlite3.connect(db_path)
    cursor = connect.cursor()
    rows = cursor.execute(f"SELECT id, name from audio_dramas")
    for r in rows:
        # bid = r[1]
        # drama_dict[bid] = r[0]
        drama_dict[r[1]] = r[0]  # name: id
    return drama_dict

def play_count_key(platform):
    if platform == 'fanjiao':
        return 'fj_play_count'
    elif platform == 'maoer':
        return 'mr_play_count'
    elif platform == 'manbo':
        return 'mb_play_count'

def get_platform_id(platform):
    if platform == 'fanjiao':
        return 'fj_id'
    elif platform == 'maoer':
        return 'mr_id'
    elif platform == 'manbo':
        return 'mb_id'

def save_dramas(platform):
    print('更新drama')
    up_id_dict = get_up_and_id()
    old_drama_id_dict = get_drama_platform_id_and_id(platform)
    old_drama_name_dict = get_drama_name_and_id()
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
                update_data = "intro = '{}', cover = '{}', status = '{}', {} = {}, {} = {}".format(
                        l['intro'].replace("'", '|') if l['intro'] != None else '', 
                        l['cover'], l['status'], play_count_key(platform),
                        int(l['playCount']) if l['playCount'] != None else -1, 
                        get_platform_id(platform), int(l['adid']) if l['adid'] != None else 0)
                if l['adid'] in old_drama_id_dict.keys() or l['name'] in old_drama_name_dict.keys():
                    # adid和name两种方式更新，旧数据可能没有adid，但可以通过name找到，adid有了之后的更新就可以通过adid
                    if l['adid'] in old_drama_id_dict.keys():
                        sql = "UPDATE audio_dramas SET {} WHERE {} = {}".format(update_data, get_platform_id(platform), l['adid'])
                    else:
                        sql = "UPDATE audio_dramas SET {} WHERE name = '{}'".format(update_data, l['name'])
                    cursor.execute(sql)
                    cursor.execute(f"SELECT id FROM audio_dramas WHERE {get_platform_id(platform)} = {l['adid']};")
                    drama_id = cursor.fetchone()[0]
                    # update up
                    if up_id:
                        cursor.execute(f'SELECT * FROM audio_dramas_up_links WHERE audio_drama_id = {drama_id}')
                        exist_link = cursor.fetchall()
                        if len(exist_link) > 0:
                            cursor.execute(f'UPDATE audio_dramas_up_links SET audio_staff_id = {up_id} WHERE audio_drama_id = {drama_id}')
                        else:
                            cursor.execute('''INSERT INTO audio_dramas_up_links (audio_drama_id, audio_staff_id) VALUES (?, ?)''', 
                            (drama_id, up_id))
                else:
                    sql = '''INSERT INTO audio_dramas (name, intro, cover, status, {}, {}) VALUES (?,?,?,?,?,?)'''\
                        .format(play_count_key(platform), get_platform_id(platform))
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
        connect.close()


def add_platforms(platform):
    print('添加drama和platform关联')
    drama_id_dict = get_drama_platform_id_and_id(platform)
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
    for p in ['maoer', 'fanjiao']:
        if p == 'maoer':
            clear_data(p)
        save_ups(p)
        save_dramas(p)
        add_platforms(p)
