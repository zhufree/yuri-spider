import scrapy


class HaitangSpider(scrapy.Spider):
    name = 'haitang'
    allowed_domains = ['www.newhtbook.com']
    start_urls = ['https://www.newhtbook.com/searchlist.php?fixlangsnd=FsedAjjT6&fixlangact=edit&selsexytype=c']
    # &searchkpage=2
    

    def __init__(self):
        self.page_count = 1
        self.base_url = 'https://www.newhtbook.com/searchlist.php?fixlangsnd=FsedAjjT6&fixlangact=edit&selsexytype=c'

    def parse(self, response):
        tds = response.css('table.uk-table tr>td')[1:]
        for td in tds:
            item = {
                'title': td.css('a:first-child>font>b::text').get(),
                'url': 'https://www.newhtbook.com' + td.css('a:first-child::attr(href)').get(),
                'author': td.css('a:nth-child(6)>font::text').get(),
                'author_url': 'https://www.newhtbook.com' + td.css('a:nth-child(6)::attr(href)').get(),
                'tags': [i.strip() for i in td.css('font:nth-child(4)::text').get().split('/')],
                'status': td.css('font:nth-child(8)::text').get(),
                'wordcount': td.css('font:nth-child(9)::text').get(),
            }
            item['tags'] = list(set(item['tags']))
            item['aid'] = item['author_url'].split('=')[-1]
            item['bid'] = 'ht' + item['url'].split('&')[-2].replace('bookid=', '')
            if item['wordcount'] == None:
                item['wordcount'] = 0
            yield item

        if len(tds) == 50:
            self.page_count += 1
            next_page = self.base_url + '&searchkpage={}'.format(self.page_count)
            yield scrapy.Request(next_page, callback=self.parse)
