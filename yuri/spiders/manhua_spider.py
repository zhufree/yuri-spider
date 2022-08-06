import scrapy


class BiliSpider(scrapy.Spider):
    name = 'bili'
    allowed_domains = ['manga.bilibili.com']
    start_urls = ['https://manga.bilibili.com/classify#/?from=manga_homepage&styles=1006&areas=1&orders=3']

    def parse(self, response):
        pass
