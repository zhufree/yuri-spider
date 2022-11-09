import scrapy

# useless
class BiliSpider(scrapy.Spider):
    name = 'bili'
    allowed_domains = ['manga.bilibili.com']
    start_urls = ['https://manga.bilibili.com/classify#/?from=manga_homepage&styles=1006&areas=1&orders=3']

    def parse(self, response):
        pass

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
                'authoName': i.css('.itemTitle::text').get(),
                'platform': 10
            }
            yield scrapy.Request(manhua['url'], self.parse_detail_page, 
                cb_kwargs=dict(data=manhua))
        if len(items) >= 48:
            print('next page')
            self.page += 1
            yield scrapy.Request(f'https://www.kuaikanmanhua.com/tag/90?region=2&page={self.page}', self.parse)
    
    def parse_detail_page(self, response, data):
        data['intro'] = response.css('.detailsBox p::text').get()
        data['cover'] = response.css('.TopicList .TopicHeader .left img.img::attr(src)').get()
        data['status'] = response.css('.bottom .text-warp div.fl:nth-child(2)::text').get()
        data['publishTime'] = response.css('.TopicItem:nth-child(1) .date span::text').get()
        yield data
