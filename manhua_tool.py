import json
import sqlite3

# steam
platform_dict = {
    'kuaikan': 10
}

platform = 'kuaikan'
db_path = '../yuri-backend/.tmp/data.db'


def get_mid_and_id():
    mid_dict = {}
    connect = sqlite3.connect(db_path)
    cursor = connect.cursor()
    rows = cursor.execute("SELECT id, m_id from manhuas")
    for r in rows:
        mid_dict[r[1]] = r[0]  # mId: id
    return mid_dict



def save_manhuas():
    print('更新manhua')
    old_mid_id_dict = get_mid_and_id()
    with open("{}-items.json".format(platform), 'r', encoding='utf-8') as f:
        lines = f.readlines()
        connect = sqlite3.connect(db_path)
        cursor = connect.cursor()
        for line in lines:
            l = json.loads(line)
            sql = ''
            try:
                if l['mId'] in old_mid_id_dict.keys():
                    update_data = "name = '{}', author_name = '{}', intro = '{}', cover = '{}', status = '{}'".format(
                        l['name'], l['authorName'],
                        l['intro'].replace("'", '|') if l['intro'] != None else '', 
                        l['cover'], l['status'])
                    sql = "UPDATE manhuas SET {} WHERE m_id = '{}'".format(update_data, l['name'])
                    cursor.execute("UPDATE manhuas SET {} WHERE m_id = '{}'".format(update_data, l['mId']))
                else:
                    cursor.execute('''INSERT INTO manhuas (name, url, m_id, cover, author_name, intro, status) VALUES (?,?,?,?,?,?,?)''',
                        (l['name'],l['url'], l['mId'], l['cover'], l['authorName'], l['intro'], l['status']))
                    # add platform link
                    cursor.execute('''INSERT OR IGNORE INTO manhuas_platform_links (manhua_id, platform_id) VALUES (?, ?)''', 
                        (cursor.lastrowid, 10)) # kuaikan only
            except Exception as e:
                print(l)
                print(sql)
                raise e
            
        connect.commit()
        connect.close()



if __name__ == '__main__':
    save_manhuas()

