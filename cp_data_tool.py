import json

def handle_json():
    with open('cp-items.json', 'r', encoding='utf-8') as f:
        json_lines = [json.loads(j) for j in f.readlines()]
        book_json = [{
            'title': j['novel_name'],
            'bid': 'cp' + j['novel_id'],
            'book_url': 'https://www.gongzicp.com/novel-{}.html'.format(j['novel_id']),
            'aid': 'cp' + j['nauthor_id'],
            'author': l['novel_author'],
            'authot_url': 'https://www.gongzicp.com/zone/author-{}.html'.format(j['nauthor_id']),
            'type': j['type_name'],
            'style': '',
            'status': j['novel_process_text'],
            'cover': j['novel_cover'],
            'wordcount': j['novel_wordnumber'].replace(',', ''),
            'publish_time': j['novel_uptime'],
            'tags': j['novel_tags'],

        } for j in json_lines]
        print(json_lines[0].keys())

if __name__ == '__main__':
    handle_json()