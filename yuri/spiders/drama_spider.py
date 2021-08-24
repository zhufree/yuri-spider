import scrapy
import time

# 长期有效
sign_dict = {
    '1': '64deb9d3e26d320f92460e0b357569b2',
    '2': 'f898dcf5804704ca9516dba1a3f80ad4',
    '3': '74ee0bdabdd0550b3e0b348f0a1439c9',
    '4': '493a49a4628019a082b09f492d33d96e',
    '5': 'f2f639b1ea4b48a9ea54087c239f644f',
    '6': '8d9525c1ddf1ecb2508b10fdb4ae36c4',
    '7': 'f37ad47162ce8b80c1e53ec4c5202800',
    '8': 'ee570da44f159bf6ad7b736c0989633e',
    '9': '28b6f0bf75b8317d20f216016ba555fe',
    '10': '5f1a14b2282e02d8ef5e5046d0d1d6f7',
    '11': '835e148804b9c55cdeba6cbf342b2fab',
    '12': '69f64e491a38dd6ba9e2e51f3b497cf8',
    '13': 'f8db257bffc5cb376862a913b7a1c4c6',
    '14': '32df54a469402bee98f0448b1d653dd2',
    '15': '24514621129da369f75ef537f595bac4',
    '16': '7963ed1eb3918d01f3081dad3f733418',
    '17': '01362edb85d7035c6bea3b9c60d422f6',
    # '18': '01362edb85d7035c6bea3b9c60d422f6',
}

class FanjiaoSpider(scrapy.Spider):
    name = 'fanjiao'
    allowed_domains = ['https://api.fanjiao.co']
    start_urls = ['https://api.fanjiao.co/walkman/api/recommend/category?cate_id=7&page={}&size=20'.format(i) for i in range(1, 18)]

    
    headers = [{
        'signature': sign_dict[str(i)]
    } for i in range(1, 18)]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, headers=self.headers[self.start_urls.index(url)] ,callback=self.parse)


    def parse(self, response):
        res_json = response.json()
        for i in res_json['data']['list']:
            drama = {
                'name': i['name'],
                'adid': i['album_id'],
                'intro': i['description'],
                'cover': i['cover'],
                'up': i['up_name'],
                'playCount': i['play'],
                'status': '已完结' if i['album_id'] < 100000 else '未知'
            }
            yield drama

class MaoerSpider(scrapy.Spider):
    name = 'maoer'
    # 0_5_1_0_0 长篇未完结
    # 0_5_2_0_0 长篇完结 8.24
    # 0_5_3_0_0 全一期
    # 0_5_4_0_0 微小剧
    start_urls = ['https://www.missevan.com/dramaapi/filter?filters=0_5_2_0_0&page=1&order=1&page_size=50']
    page_count = 1
    base_url = 'https://www.missevan.com/dramaapi/filter?filters=0_5_2_0_0&page={}&order=1&page_size=50'
    handle_httpstatus_list = [418]

    def get_status(self, integrity):
        if integrity == 1:
            return '更新至'
        else:
            return '已完结'

    def parse(self, response):
        res_json = response.json()
        has_more = res_json['info']['pagination']['has_more']
        for i in res_json['info']['Datas']:
            drama = {
                'name': i['name'],
                'adid': i['id'],
                'cover': i['cover'],
                'status': self.get_status(i['integrity']) + '|' + i['newest'],
            }
            yield scrapy.Request('https://www.missevan.com/dramaapi/getdrama?drama_id={}'.format(i['id']), self.get_drama, 
                cb_kwargs=dict(data=drama))
            # yield item

        if has_more:
            self.page_count = self.page_count + 1
            next_page = self.base_url.format(self.page_count)
            yield scrapy.Request(next_page, callback=self.parse)

    def get_drama(self, response, data):
        if response.status == 418:
            print(response.url)
        else:
            res_json = response.json()
            data['intro'] = res_json['info']['drama']['abstract']
            data['playCount'] = res_json['info']['drama']['view_count']
            eps = res_json['info']['episodes']['episode']
            # no up data, open a sound to get up info
            if len(eps) > 0:
                sound_id = eps[0]['sound_id']
                yield scrapy.Request('https://www.missevan.com/sound/getsound?soundid={}'.format(sound_id), self.get_sound, 
                        cb_kwargs=dict(data=data))
            else:
                yield data


    def get_sound(self, response, data):
        if response.status == 418:
            print(response.url)
        else:
            res_json = response.json()
            if 'user' in res_json['info'].keys():
                username = res_json['info']['user']['username']
                data['up'] = username
            yield data


