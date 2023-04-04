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
# 3 有声书
# 5, 6 电台
# 7 广播剧，首页的广播剧tab，但是数据不全
https://api.fanjiao.co/walkman/api/recommend/major?page=1&size=20&type=4 新剧速递
https://api.fanjiao.co/walkman/api/recommend/major?page=1&size=20&type=3 精品周更
'''

# 有ip拦截 2023.4.3
class FanjiaoSpider(scrapy.Spider):
    name = 'fanjiao'
    # allowed_domains = ['https://api.fanjiao.co']
    start_urls = ['https://api.fanjiao.co/walkman/api/recommend/category?cate_id=7&page={}&size=50'.format(i) for i in range(1, 12)]+ \
        ['https://api.fanjiao.co/walkman/api/recommend/major?page=1&size=20&type=4', 'https://api.fanjiao.co/walkman/api/recommend/major?page=1&size=20&type=3']

    def start_requests(self):
        for url in self.start_urls:
            param = url.split('?')[-1] + '879f30c4b1641142c6192acc23cfb733'
            sign = md5(param.encode('utf-8')).hexdigest()
            headers = {
                'signature': sign
            }
            yield scrapy.Request(url, headers=headers, callback=self.parse)


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
            if 'subtitle' in i.keys():
                drama['subtitle'] = i['subtitle']
            if drama['up'] == '轻之声GL广播剧社':
                drama['up'] = '轻之声广播剧社'
            if drama['up'] == '桂圆翊宝':
                drama['up'] = '桂圆翊宝（张宇琦）'
            if i['album_id'] < 100100:
                yield drama
            else:
                audio_list_url = 'https://api.fanjiao.co/walkman/api/album/audio?album_id={}'.format(i['album_id'])
                param = audio_list_url.split('?')[-1] + '879f30c4b1641142c6192acc23cfb733'
                sign = md5(param.encode('utf-8')).hexdigest()
                headers = {
                    'signature': sign
                }
                time.sleep(1)
                yield scrapy.Request(audio_list_url, headers=headers, callback=self.get_audio_list, cb_kwargs=dict(data=drama))
    
    # check subtitle
    def get_audio_list(self, response, data):
        ep_json = response.json()
        has_sub = False
        if 'data' in ep_json.keys() and 'audios_list' in ep_json['data'].keys():
            for audio in ep_json['data']['audios_list']:
                if audio['subtitle'] != '':
                    has_sub = True
                    break
        data['hasSub'] = has_sub
        yield data

# 有ip拦截，少抓点 2023.4.3
class MaoerSpider(scrapy.Spider):
    name = 'maoer'
    # types = [1, 2, 3, 4]
    series_not_finished = '1'
    series_finished = '2'
    one_ep = '3'
    small_ep = '4'
    current_type = '3'
    # 0_5_1_0_0 长篇未完结 2022.11.30
    # 0_5_2_0_0 长篇完结 2023.3.6
    # 0_5_3_0_0 全一期 8.31 2023.4.3
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

# tingji spider
# 76 2023.4.3
class TingjiSpider(scrapy.Spider):
    name = 'tingji'
    allowed_domains = ['www.himehear.com']  # Replace with the actual domain
    start_urls = ['https://www.himehear.com/tjapp/v1/works/list?category=drama&pageNum=1&pageSize=100&radioType=bh']  # Replace with the actual start URL
    cdn_prefix = 'https://tingjifm-pub.oss-cn-shenzhen.aliyuncs.com/'
    pageIndex = 1

    def parse(self, response):
        res_json = response.json()
        for i in res_json['result']:
            # "radioState": 1 更新中, 2 已完结
            # "needFee": 1 免费 2,付费
            drama = {
                'name': i['radioDramaName'],
                'adid': i['id'],
                'intro': i['introduction'],
                'cover': self.cdn_prefix + i['radioImg'],
                'up': i['studioName'],
                'playCount': i['listenedCount'],
                'status': '更新中' if i['radioState'] == 1 else "已完结",
                'isCommercial': True if i['needFee'] == 2 else False,
            }
            audio_list_url = 'https://www.himehear.com/tjapp/v1/works/drama/detail?radioId={}'.format(i['id'])
            yield scrapy.Request(audio_list_url, callback=self.parse_detail, cb_kwargs=dict(data=drama))
    # parse detail
    def parse_detail(self, response, data):
        ep_json = response.json()
        has_sub = False
        if ep_json['code'] == 0 and 'partDramas' in ep_json['result'].keys():
            for audio in ep_json['result']['partDramas']:
                if 'subtitlePath' in audio.keys():
                    has_sub = True
                    break
        data['hasSub'] = has_sub
        yield data


# Manbo spider
class ManboSpider(scrapy.Spider):
    name = 'manbo'
    page = 1
    # Add allowed_domains and start_urls according to the actual domain and start URL
    start_urls = ['https://api.kilamanbo.com/api/v389/radio/drama/aggregation/content?categoryId=1&endStatus=0&labelId=691358&pageNo=1&pageSize=200&payType=0&sort=1']
    base_url = 'https://api.kilamanbo.com/api/v389/radio/drama/aggregation/content?categoryId=1&endStatus=0&labelId=691358&pageSize=200&payType=0&sort=1' #&pageNo=1
    
    def parse(self, response):
        res_json = response.json()
        for i in res_json['b']['radioDramaRespList']:
            # "endStatus": 1 完结 2连载
            # "payType": 1 免费 2 付费 3 会员免费
            drama = {
                'name': i['title'],
                'adid': i['radioDramaId'],
                'intro': i['desc'],
                'cover': i['coverPic'],
                'up': i['ownerResp']['nickname'],
                'status': '已完结' if i['endStatus'] == 1 else '连载中',
                'isCommercial': False if i['payType'] == 1 else True,
            }
            audio_list_url = 'https://manbo.hongdoulive.com/web_manbo/dramaDetail?dramaId={}'.format(i['radioDramaId'])
            yield scrapy.Request(audio_list_url, callback=self.parse_detail, cb_kwargs=dict(data=drama))
        if len(res_json['b']['radioDramaRespList']) == 200:
            self.page += 1
            next_page_url = self.base_url + f'&pageNo={self.page}'
            yield scrapy.Request(next_page_url, callback=self.parse)

    def parse_detail(self, response, data):
        detail_json = response.json()
        has_sub = False
        if detail_json['code'] == 200:
            data['playCount'] = detail_json['data']['watchCount']
            data['publishTime'] = detail_json['data']['createTime'] # timestamp
            for audio in detail_json['data']['setRespList']:
                if audio['setLrcUrl'] != '':
                    has_sub = True
                    break
        data['hasSub'] = has_sub
        yield data
