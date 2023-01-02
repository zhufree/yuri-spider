import json
import sqlite3


platform_dict = {
    'jjwxc': 1,
    'changpei': 2,
    'haitang': 7,
    'po18': 8,
    'popo': 12
}

db_path = '../yuri-backend/.tmp/data.db'


# 获取作者id {'aid': id}
def get_author_and_id():
    author_dict = {}
    connect = sqlite3.connect(db_path)
    cursor = connect.cursor()
    rows = cursor.execute("SELECT id, aid from authors")
    for r in rows:
        _id = r[0]
        aid = r[1]
        author_dict[aid] = _id
    return author_dict


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


def get_book_and_id():
    book_dict = {}
    connect = sqlite3.connect(db_path)
    cursor = connect.cursor()
    rows = cursor.execute("SELECT id, bid, title from books")
    for r in rows:
        _id = r[0]
        bid = r[1]
        book_dict[bid] = _id
    return book_dict

# 先录入作者，tag，再录入book，匹配作者和tag id
def save_author(platform):
    print('更新作者：')
    author_dict = {}
    with open("{}-items.json".format(platform), 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for l in lines:
            d = json.loads(l)
            author_name = d['author']
            author_url = d['author_url']
            aid = d['aid']
            if aid not in author_dict.keys():
                author_dict[aid] = {
                    'url': author_url,
                    'aid': aid,
                    'name': author_name
                }
    connect = sqlite3.connect(db_path)
    cursor = connect.cursor()
    old_authors_dict = get_author_and_id()
    for aid in author_dict.keys():
        if aid in old_authors_dict.keys():
            # update old data
            update_data = "url = '{}', name = '{}'".format(author_dict[aid]['url'], author_dict[aid]['name'])
            cursor.execute("UPDATE authors SET {} WHERE aid = '{}'".format(update_data, aid))
        else:
            cursor.execute(
                '''INSERT INTO authors (name, url, aid) VALUES (?,?,?)''',
                (author_dict[aid]['name'],author_dict[aid]['url'],author_dict[aid]['aid']))
            # add platform link
            cursor.execute(f'INSERT INTO authors_platform_links (author_id, platform_id) VALUES (?,?)', (cursor.lastrowid, platform_dict[platform]))
    connect.commit()
    connect.close()


def save_tags(platform):
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


def save_books(platform):
    print('更新novel')
    author_id_dict = get_author_and_id()
    old_book_id_dict = get_book_and_id()
    with open("{}-items.json".format(platform), 'r', encoding='utf-8') as f:
        lines = f.readlines()
        connect = sqlite3.connect(db_path)
        cursor = connect.cursor()
        for line in lines:
            l = json.loads(line)
            if '未' in l['status'] or '中' in l['status']:
                l['status'] = '连载'
            elif '完' in l['status']:
                l['status'] = '完结'
            elif l['status'] == '暂停':
                l['status'] = '断更'

            if l['aid'] in author_id_dict.keys():
                author_id = author_id_dict[l['aid']]
            else:
                author_id = 0
            sql = ''
            try:
                if l['bid'] in old_book_id_dict.keys():
                    # 已有，更新数据
                    # collectionCount 负数不录入
                    update_data = "title = '{}', bid = '{}', url = '{}', cover = '{}', description = '{}', \
                    style = '{}', type = '{}', status = '{}', publish_time = '{}', wordcount = {}, \
                    collection_count = {}, search_keyword = '{}'".format(
                        l['title'].replace("'", '|'), l['bid'], l['book_url'], l['cover'], l['description'].replace("'", '|'), \
                        l['style'], l['type'], l['status'], l['publish_time'], 
                        int(l['wordcount']) if l['wordcount'] != None else -1, 
                        int(l['collectionCount']) if l['collectionCount'] != None else -1, 
                        l['searchKeyword'].replace("'", '|') if l['searchKeyword'] != None else '')
                    sql = "UPDATE books SET {} WHERE bid = '{}'".format(update_data, l['bid'])
                    cursor.execute("UPDATE books SET {} WHERE bid = '{}'".format(update_data, l['bid']))
                    book_id = old_book_id_dict[l['bid']]
                    cursor.execute(f"UPDATE books_author_links SET author_id = '{author_id}' WHERE book_id = '{book_id}'")
                else:
                    # 插入新数据
                    cursor.execute('''INSERT INTO books (title, bid, url, cover, description, style, type, status, publish_time, \
                        wordcount, collection_count, search_keyword) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)''',
                        (l['title'].replace("'", '|'), l['bid'], l['book_url'], l['cover'], l['description'].replace("'", '|'), l['style'], l['type'], l['status'],
                        l['publish_time'],
                        int(l['wordcount']) if l['wordcount'] != None else -1, 
                        int(l['collectionCount']) if l['collectionCount'] != None else -1,
                        l['searchKeyword']))
                    book_id = cursor.lastrowid
                    # insert author link and platform link
                    cursor.execute(f'INSERT INTO books_author_links (book_id, author_id) VALUES (?,?)', (book_id, author_id))
                    cursor.execute(f'INSERT INTO books_platform_links (book_id, platform_id) VALUES (?,?)', (book_id, platform_dict[platform]))
            except Exception as e:
                print(sql)
                raise e
            
        connect.commit()
        connect.close()


def add_tags(platform):
    print('添加novel和tag关联')
    tag_id_dict = get_tag_and_id() # dict from db
    book_id_dict = get_book_and_id()
    connect = sqlite3.connect(db_path)
    cursor = connect.cursor()
    rows = cursor.execute("SELECT book_id, tag_id from books_tags_links")
    book_tag_dict = {}
    for r in rows:
        book_id = r[0]
        tag_id = r[1]
        if book_id in book_tag_dict.keys():
            book_tag_dict[book_id].append(tag_id)
        else:
            book_tag_dict[book_id] = [tag_id]
    with open("{}-items.json".format(platform), 'r', encoding='utf-8') as f:
        lines = f.readlines()
        connect = sqlite3.connect(db_path)
        cursor = connect.cursor()
        for line in lines:
            item = json.loads(line)
            book_id = book_id_dict[item['bid']] # insert book by book
            tag_ids = []
            for t in item['tags']: 
                if t in tag_id_dict.keys(): # get all tags for one book
                    tag_ids.append(tag_id_dict[t])
            for tag_id in tag_ids: # insert book-tag relation one by one
                if book_id not in book_tag_dict.keys() or tag_id not in book_tag_dict[book_id]:
                    # check if the tag and book connection exist
                    cursor.execute("INSERT INTO books_tags_links (book_id, tag_id) \
                    VALUES ({}, {})".format(book_id, tag_id))
        connect.commit()
        connect.close()


if __name__ == '__main__':
    platforms = [
        'jjwxc',
        'changpei',
        'haitang',
        'po18',
        'popo'
    ]
    for p in platforms:
        save_author(p)
        save_tags(p)
        save_books(p)
        add_tags(p)
