import scrapy, json

# 2023.4.4
class BiliSpider(scrapy.Spider):
    name = 'bili'
    allowed_domains = ['manga.bilibili.com']
    start_urls = ['https://manga.bilibili.com/twirp/comic.v1.Comic/ClassPage']
    data = {
        "isFree" : -1,
        "areaId" : 1, # 大陆
        "orientation" : 0,
        "pageNum" : 1,
        "tagId" : 1369,
        "comicIdFrom" : 27287,
        "type" : -1,
        "styleId" : -1,
        "order" : 0,
        "isRookie" : False,
        "isFinish" : -1,
        "pageSize" : 50
    }

    def start_requests(self):
        # Send a POST request with the data
        yield scrapy.Request(
            url=self.start_urls[0],
            method='POST',
            body=json.dumps(self.data),
            headers={'Content-Type':'application/json'},
            callback=self.parse
        )
    def parse(self, response):
        list_json = response.json()
        if list_json['code'] == 0:
            for i in list_json['data']:
                manhua = {
                    'mId': f'mc{i["season_id"]}',
                    'name': i['title'],
                    'url': f'https://manga.bilibili.com/detail/{i["season_id"]}',
                    'cover': i['horizontal_cover'],
                    # 'authorName': i.css('.author::text').get().strip(),
                    'platform': 9
                }
                detail_url = 'https://manga.bilibili.com/twirp/comic.v1.Comic/ComicDetail?device=pc'
                yield scrapy.Request(
                    url=detail_url,
                    method='POST',
                    body=json.dumps({'comic_id': i["season_id"]}),
                    headers={'Content-Type':'application/json'},
                    callback=self.parse_detail,
                    cb_kwargs=dict(data=manhua)
                )

    def parse_detail(self, response, data):
        detail_json = response.json()
        if detail_json['code'] == 0:
            manhua = detail_json['data']
            data['authorName'] = '/'.join(manhua['author_name'])
            if manhua['release_time'] != '' and len(manhua['release_time']) > 4:
                data['publishTime'] = manhua['release_time'].replace('.', '-')
            else:
                publish_time = ''
                if 'ep_list' in manhua.keys() and len(manhua['ep_list']) > 0:
                    publish_time = manhua['ep_list'][-1]['pub_time']
                data['publishTime'] = publish_time
        yield data

# 2022.11.9
class KuaikanSpider(scrapy.Spider):
    name = 'kuaikan'
    allowed_domains = ['www.kuaikanmanhua.com']
    start_urls = ['https://www.kuaikanmanhua.com/tag/90?region=2'] # region2 国漫
    base_url = 'https://www.kuaikanmanhua.com'
    page = 1

    def parse(self, response):
        items = response.css('.ItemSpecial')
        for i in items:
            url_part = i.css('.itemLink::attr(href)').get()
            manhua = {
                'mId': 'kk' + url_part.split('/')[-1],
                'name': i.css('.itemTitle::text').get(),
                'url': self.base_url + url_part,
                'cover': i.css('img.img::attr(src)').get(),
                'authorName': i.css('.author::text').get().strip(),
                'platform': 10
            }
            yield scrapy.Request(manhua['url'], self.parse_detail_page, 
                cb_kwargs=dict(data=manhua))
        if len(items) >= 40:
            print('next page')
            self.page += 1
            yield scrapy.Request(f'https://www.kuaikanmanhua.com/tag/90?region=2&page={self.page}', self.parse)
    
    def parse_detail_page(self, response, data):
        data['intro'] = response.css('.detailsBox p::text').get()
        data['cover'] = response.css('.TopicList .TopicHeader .left img.img::attr(src)').get()
        data['status'] = response.css('.bottom .text-warp div.fl:nth-child(2)::text').get()
        data['publishTime'] = response.css('.TopicItem:nth-child(1) .date span::text').get()
        yield data
