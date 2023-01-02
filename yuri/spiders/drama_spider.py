import scrapy
import time
from hashlib import md5

'''
2022.11.30
"paging": {
    "page_size": 50,
    "page": 1,
    "total": 491
}
'''
class FanjiaoSpider(scrapy.Spider):
    name = 'fanjiao'
    allowed_domains = ['https://api.fanjiao.co']
    start_urls = ['https://api.fanjiao.co/walkman/api/recommend/category?cate_id=7&page={}&size=50'.format(i) for i in range(1, 12)]

    def start_requests(self):
        for url in self.start_urls:
            param = url.split('?')[-1] + '879f30c4b1641142c6192acc23cfb733'
            sign = md5(param.encode('utf-8')).hexdigest()
            headers = {
                'signature': sign
            }
            yield scrapy.Request(url, headers=headers ,callback=self.parse)


    def parse(self, response):
        res_json = response.json()
        for i in res_json['data']['list']:
            drama = {
                'name': i['name'],
                'adid': i['album_id'],
                'intro': i['description'],
                'cover': i['square'],
                'up': i['up_name'],
                'playCount': i['play'],
                'status': '更新到' + i['new_audio_name']
            }
            if drama['up'] == '轻之声GL广播剧社':
                drama['up'] = '轻之声广播剧社'
            if drama['up'] == '桂圆翊宝':
                drama['up'] = '桂圆翊宝（张宇琦）'
            yield drama


# 有ip拦截，少抓点
class MaoerSpider(scrapy.Spider):
    name = 'maoer'
    # types = [1, 2, 3, 4]
    series_not_finished = '1'
    series_finished = '2'
    one_ep = '3'
    small_ep = '4'
    current_type = '2'
    # 0_5_1_0_0 长篇未完结 2022.11.30
    # 0_5_2_0_0 长篇完结 8.24
    # 0_5_3_0_0 全一期 8.31
    # 0_5_4_0_0 微小剧 2022.11.2 无数据
    start_urls = [f'https://www.missevan.com/dramaapi/filter?filters=0_5_{current_type}_0_0&page=1&order=1&page_size=50']
    page_count = 1
    base_url = f'https://www.missevan.com/dramaapi/filter?filters=0_5_{current_type}_0_0&order=1&page_size=50'
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
            time.sleep(1)

        if has_more:
            self.page_count = self.page_count + 1
            next_page = self.base_url + f'&page={self.page_count}'
            time.sleep(1)
            yield scrapy.Request(next_page, callback=self.parse)

    def get_drama(self, response, data):
        if response.status == 418:
            print(response.url)
        else:
            res_json = response.json()
            data['intro'] = res_json['info']['drama']['abstract']
            if data['intro'] == None:
                return
            data['playCount'] = res_json['info']['drama']['view_count']
            data['up'] = res_json['info']['drama']['author']
            eps = res_json['info']['episodes']['episode']
            if len(eps) > 0:
                ep_id = eps[0]['sound_id']
                yield scrapy.Request(f'https://www.missevan.com/sound/getsound?soundid={ep_id}', self.get_sound,
                    cb_kwargs=dict(data=data))
            else:
                return

    def get_sound(self, response, data):
        if response.status == 418:
            print(response.url)
        else:
            ep_json = response.json()
            if 'info' in ep_json and 'user' in ep_json['info']:
                data['up'] = ep_json['info']['user']['username']
        yield data
