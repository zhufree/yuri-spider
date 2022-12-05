import sqlite3
db_path = '../yuri-backend/.tmp/data.db'

def check_book_with_no_author():
    connect = sqlite3.connect(db_path)
    cursor1 = connect.cursor()
    cursor2 = connect.cursor()
    book_id_rows = cursor1.execute("SELECT id from books")
    for row in book_id_rows:
        book_id = row[0]
        author_id_rows = cursor2.execute(f"SELECT author_id from books_author_links WHERE book_id = {book_id}")
        if len(list(author_id_rows)) == 0:
            print(book_id)

def delete_author_with_no_book():
    connect = sqlite3.connect(db_path)
    cursor1 = connect.cursor()
    cursor2 = connect.cursor()
    cursor3 = connect.cursor()
    author_id_rows = cursor1.execute("SELECT id from authors")
    for row in author_id_rows:
        author_id = row[0]
        book_id_rows = cursor2.execute(f"SELECT book_id from books_author_links WHERE author_id = {author_id}")
        if len(list(book_id_rows)) == 0:
            cursor3.execute(f"DELETE FROM authors WHERE id = {author_id}")
    connect.commit()
    connect.close()

if __name__ == '__main__':
    # check_book_with_no_author()
    delete_author_with_no_book()