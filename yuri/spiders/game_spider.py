# 橙光百合api
# level： L1/L2/L3/
# 456编推/经典
# type: 1-鲜花 2-新作 3-更新 4-完结 5-随机
import requests
from pyquery import PyQuery as pq
import json

test_url = 'http://www.66rpg.com/game/1495539'
list_page_url = 'http://www.66rpg.com/pcchannel/t_45/SIfn06Mh484.shtml'
api_url = 'http://www.66rpg.com/ajax/Channel/get_channel_cross?tid=12558&level={}&type={}'

chengguang_items = []
# web page
def get_66rpg_list():
	global chengguang_items
	doc = pq(list_page_url)
	li = doc('.classic-contentList li')
	for l in li.items():
		name = l('.contentList-title').text()
		if name != '' and name not in [i['name'] for i in chengguang_items]:
			cover = l('.contentList-cover>img').attr('data-original')
			url = 'https:' + l('a').attr('href')
			author = l('.contentList-name>a>span').text()
			author_url = 'https:' + l('.contentList-name>a').attr('href')
			item = {
				'name': name,
				'cover': cover,
				'url': url,
				'gId': 'cg' + url.split('/')[-1],
				'platform': 11,
				'author': author,
				'authorUrl': author_url
			}
			detail = get_chengguang_detail(url)
			item.update(detail)
			chengguang_items.append(item)

# api
def get_66rpg_api_list():
	global chengguang_items
	header = {'Referer': 'http://www.66rpg.com/pcchannel/t_45/SIfn06Mh484.shtml'}
	for l in [1, 2, 3, '456']:
		for t in [1, 2, 3, 4, 5]:
			res = requests.get(api_url.format(l, t), headers=header)
			data = res.json()
			if data['status'] == 1:
				data_list = data['data']['data']
				for i in data_list:
					item = {
						'name': i['cms_game_name_tv'],
						'cover': i['cms_game_iv'],
						'url': 'https://www.66rpg.com/game/' + i['gindex'],
						'gId': 'cg' + i['gindex'],
						'author': i['cms_game_author_name_tv'],
						'authorUrl': 'https://www.66rpg.com/friend/' + i['author_uid']
					}
					if item['name'] != '' and item['name'] not in [i['name'] for i in chengguang_items]:
						detail = get_chengguang_detail(item['url'])
						if detail != None:
							item.update(detail)
						chengguang_items.append(item)

def get_chengguang_detail(game_url):
	print(game_url)
	try:
		doc = pq(game_url)
		name = doc('.game-info>.title>span').text()
		tags = doc('.tags > .tag').text().split(' ')
		if '完结' in tags:
			status = '完结'
		else:
			status = '未完结'
		intro = doc('.content>.inner').text()
		publish_time = doc('i.release-time').parent().next().text()
		collection_count = doc('span.fav_count').text()
		return {
			'name': name,
			'tags': tags,
			'status': status,
			'intro': intro,
			'publishTime': publish_time,
			'collectionCount': collection_count
		}
	except Exception as e:
		print(e)
	finally:
		pass
	


def save_game_items():
	global chengguang_items
	with open('{}-items.json'.format('chengguang'), 'w', encoding='utf-8') as f:
		for i in chengguang_items:
			f.write(json.dumps(i, ensure_ascii=False) + '\n')


if __name__ == '__main__':
	get_66rpg_list()
	get_66rpg_api_list()
	save_game_items()
