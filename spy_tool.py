import json
import requests
import sqlite3


platform_dict = {
    'jjwxc': 1,
    'changpei': 2,
    'haitang': 3
}

platform = 'jjwxc'
db_path = 'E:/yuri-backend/.tmp/data.db'

# 先录入作者，tag，再录入book，匹配作者和tag id
def save_author():
    print('更新作者：')
    author_dict = {}
    with open("items.json", 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for l in lines:
            d = json.loads(l)
            author_name = d['author']
            author_url = d['author_url']
            aid = d['aid']
            if author_name not in author_dict.keys():
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
            update_data = "url = '{}', aid = '{}', platform = {}".format(author_dict[aid]['url'], author_dict[aid]['aid'], platform_dict[platform])
            cursor.execute("UPDATE authors SET {} WHERE aid = '{}'".format(update_data, aid))
        else:
            insert_data = "('{}', '{}', '{}', {})".format(author_dict[aid]['name'],author_dict[aid]['url'],author_dict[aid]['aid'],platform_dict[platform])
            cursor.execute("INSERT INTO authors (name, url, aid, platform) \
                VALUES " + insert_data)
    connect.commit()
    connect.close()


def save_tags():
    print('更新tag')
    tag_list = []
    old_tag_list = get_tag_and_id()
    with open("items.json", 'r', encoding='utf-8') as f:
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
            cursor.execute("INSERT OR IGNORE INTO tags (name) VALUES ('{}')".format(t))
    connect.commit()
    connect.close()


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

def save_books():
    print('更新novel')
    author_id_dict = get_author_and_id()
    tag_id_dict = get_tag_and_id()
    old_book_id_dict = get_book_and_id()
    with open("items.json", 'r', encoding='utf-8') as f:
        lines = f.readlines()
        connect = sqlite3.connect(db_path)
        cursor = connect.cursor()
        for line in lines:
            l = json.loads(line)
            if l['aid'] in author_id_dict.keys():
                author_id = author_id_dict[l['aid']]
            else:
                author_id = 0
            if l['bid'] in old_book_id_dict.keys():
                update_data = "title = '{}', bid = '{}', url = '{}', cover = '{}', style = '{}', type = '{}', status = '{}', publishTime = '{}', wordcount = {}, collectionCount = {}, author = {}, platform = {}".format(
                    l['title'], l['bid'], l['book_url'], l['cover'], l['style'], l['type'], l['status'],
                    l['publish_time'], int(l['wordcount']), int(l['collectionCount']),
                    author_id, platform_dict[platform])
                sql = "UPDATE books SET {} WHERE bid = '{}'".format(update_data, l['bid'])
                cursor.execute("UPDATE books SET {} WHERE bid = '{}'".format(update_data, l['bid']))
            else:
                insert_data = "('{}', '{}', '{}', '{}', '{}','{}', '{}', '{}', {}, {}, {}, {})".format(
                    l['title'], l['bid'], l['book_url'], l['cover'], l['style'], l['type'], l['status'],
                    l['publish_time'], int(l['wordcount']), int(l['collectionCount']),
                    author_id, platform_dict[platform])
                cursor.execute("INSERT INTO books (title, bid, url, cover, style, type, status, publishTime, \
                    wordcount, collectionCount, author, platform) VALUES " + insert_data)
        connect.commit()
        connect.close()


def add_tags():
    print('添加novel和tag关联')
    tag_id_dict = get_tag_and_id()
    book_id_dict = get_book_and_id()
    connect = sqlite3.connect(db_path)
    cursor = connect.cursor()
    rows = cursor.execute("SELECT book_id, tag_id from books_tags__tags_books")
    book_tag_dict = {}
    for r in rows:
        book_id = r[0]
        tag_id = r[1]
        if book_id in book_tag_dict.keys():
            book_tag_dict[book_id].append(tag_id)
        else:
            book_tag_dict[book_id] = []
    with open("items.json", 'r', encoding='utf-8') as f:
        lines = f.readlines()
        connect = sqlite3.connect(db_path)
        cursor = connect.cursor()
        for line in lines:
            item = json.loads(line)
            book_id = book_id_dict[item['bid']] # insert book by book
            tag_ids = []
            for t in item['tags']: # get all tags for one book
                tag_ids.append(tag_id_dict[t])
            for tag_id in tag_ids: # insert book-tag relation one by one
                if book_id not in book_tag_dict.keys() or tag_id not in book_tag_dict[book_id]:
                    # check if the tag and book connection exist
                    cursor.execute("INSERT INTO books_tags__tags_books (book_id, tag_id) \
                    VALUES ({}, {})".format(book_id, tag_id))
        connect.commit()
        connect.close()


def add_platform():
    connect = sqlite3.connect(db_path)
    cursor = connect.cursor()
    cursor.execute("INSERT INTO platforms (name) \
                    VALUES ('{}')".format('晋江文学城'))
    connect.commit()
    connect.close()
if __name__ == '__main__':
    # save_author()
    # save_tags()
    save_books()
    # add_tags()
    # add_platform()
