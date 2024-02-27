from pyquery import PyQuery as pq
import httpx
import sqlite3

db_path = '../yuri-backend/.tmp/data.db'
connect = sqlite3.connect(db_path)
cursor = connect.cursor()

def get_adapted_str(_type):
	if _type == '广播剧':
		return 'audio_drama'
	elif '漫画' in _type:
		return 'manhua'
	elif '游戏' in _type:
		return 'game'
	elif '有声' in _type:
		return 'audio_book'
		

for i in range(1, 8):
	body = httpx.get(f'https://www.jjwxc.net/videoIntroduction.php?&page={i}')
	body.encoding = 'gb2312'
	doc = pq(body.text)
	table = doc('.main>ul>table:nth-child(1)')
	# print(list(table)[0])
	rows = list(table('tr').items())

	for row in rows[2:-1]:
		style = row('td:nth-child(5)').text()
		if '百合' in style:
			book = {
				'id': (i-1)*500 + int(row('td:nth-child(1)').text()),
				'type': row('td:nth-child(2)').text(),
				'title':row('td:nth-child(3)').text(),
				'author': row('td:nth-child(4)').text(),
				'url': 'https:' + row('td:nth-child(3) >a').attr('href'),
				'style': style,
			}
			# get bid
			print(book)
			bid = 'jj' + book['url'].split('=')[-1]
			adapted_str = get_adapted_str(book['type'])
			if adapted_str == None:
				print('暂不录入', book['type'])
				continue
			# check if book exist
			exist_book = None
			copyright_id = None
			book_rows = cursor.execute("SELECT id, bid, title from books")
			for row in book_rows:
				if row[1] == bid:
					exist_book = row[0]
			if exist_book != None:
				# if exist, check if copyright info exist
				copyright_rows = cursor.execute(f"SELECT copyright_info_id FROM copyright_infos_book_links WHERE book_id = {exist_book}")
				for row in copyright_rows:
					copyright_id = row[0]
				if copyright_id:
					# if exist, update data and update time
					cursor.execute(f'UPDATE copyright_infos SET adapted_{adapted_str} = true, jj_index = {book["id"]} WHERE id = {copyright_id}')
				else:
					# if not exist, create new copyright info
					cursor.execute(f'INSERT INTO copyright_infos (adapted_{adapted_str}, jj_index) VALUES (true, {book["id"]})')
					copyright_id = cursor.lastrowid
					cursor.execute(f'INSERT INTO copyright_infos_book_links (copyright_info_id, book_id) VALUES (?, ?)', (copyright_id, exist_book))
			else:
				# if not exist, print book name and url for add book manually
				print(book['title'], book['url'], 'not exist')
connect.commit()
connect.close()

