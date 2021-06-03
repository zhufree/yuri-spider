import scrapy


class CpSpider(scrapy.Spider):
    name = 'cp'
    allowed_domains = ['gongzicp.com']
    start_urls = ['https://www.gongzicp.com/novel/getNovelList?page=1&type_id=17&field=novel_allpopu&order=desc']
    
    def __init__(self):
        self.page_count = 1
        self.base_url = 'https://www.gongzicp.com/novel/getNovelList?type_id=17&field=novel_allpopu&order=desc'

    def parse(self, response):
        res_json = response.json()
        novel_list = res_json['data']['list']
        for i in novel_list:
            yield i
            
        if len(novel_list) == 10:
            self.page_count += 1
            next_page = self.base_url + '&page={}'.format(self.page_count)
            yield scrapy.Request(next_page, callback=self.parse)