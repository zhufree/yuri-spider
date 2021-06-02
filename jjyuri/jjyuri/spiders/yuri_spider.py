import scrapy


class YuriSpider(scrapy.Spider):
    name = "yuri"
    # 793页

    start_urls = [
        'http://www.jjwxc.net/bookbase.php?xx3=3',
    ]

    def parse(self, response):
        current_page_list = []
        for tr in response.css('table.cytable tr')[1:]:
            current_novel = {
                'author': tr.css('td:first-child>a::text').get().strip(),
                'author_url': 'http://www.jjwxc.net/' + tr.css('td:first-child>a::attr(href)').get().strip(),
                'title': tr.css('td:nth-child(2)>a::text').get().strip(),
                'book_url':'http://www.jjwxc.net/' +  tr.css('td:nth-child(2)>a::attr(href)').get().strip(),
                'type': tr.css('td:nth-child(3)::text').get().strip(),  # 原创-百合-近代现代-爱情
                'style': tr.css('td:nth-child(4)::text').get().strip(),  # 暗黑
                'status': tr.css('td:nth-child(5)::text').get().strip(),
                'wordcount': tr.css('td:nth-child(6)::text').get().strip(),
                'publish_time': tr.css('td:nth-child(8)::text').get().strip(),
            }
            current_page_list.append(current_novel)
            # open novel page for more info
            yield scrapy.Request(current_novel['book_url'], self.parse_novel_page, 
                cb_kwargs=dict(data=current_novel))

        # next page
        # next_page = response.css('div.pageArea a:nth-child(2)::attr(href)').get()
        # if len(current_page_list) == 100:
        #     next_page = response.urljoin(next_page)
        #     yield scrapy.Request(next_page, callback=self.parse)

    def parse_novel_page(self, response, data):
        data['collectionCount'] = response.css('span[itemprop="collectedCount"]::text').get()
        data['tags'] = response.css('div.smallreadbody a::text').getall()
        yield data