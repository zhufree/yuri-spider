import scrapy


class YuriSpider(scrapy.Spider):
    name = "jjwxc"
    # name = "jjwxc-list"
    # 804页

    start_urls = [
        'http://www.jjwxc.net/bookbase.php?xx3=3',
    ]

    def parse(self, response):
        current_page_list = []
        for tr in response.css('table.cytable tr')[1:]:
            current_novel = {
                'author': tr.css('td:first-child>a::text').get().strip(),
                'author_url': 'http://www.jjwxc.net/' + tr.css('td:first-child>a::attr(href)').get().strip(),
                'title': tr.css('td:nth-child(2)>a::text').get().strip() if tr.css('td:nth-child(2)>a::text').get() != None else '***',
                'book_url':'http://www.jjwxc.net/' +  tr.css('td:nth-child(2)>a::attr(href)').get().strip(),
                'type': tr.css('td:nth-child(3)::text').get().strip(),  # 原创-百合-近代现代-爱情
                'style': tr.css('td:nth-child(4)::text').get().strip(),  # 暗黑
                'status': [i.strip() for i in tr.css('td:nth-child(5) *::text').getall() if len(i.strip()) > 0][0],
                'wordcount': tr.css('td:nth-child(6)::text').get().strip(),
                'publish_time': tr.css('td:nth-child(8)::text').get().strip(),
            }
            current_novel['bid'] = 'jj' + current_novel['book_url'].split('=')[-1]
            current_novel['aid'] = 'jj' + current_novel['author_url'].split('=')[-1]
            current_page_list.append(current_novel)
            # open novel page for more info
            yield scrapy.Request(current_novel['book_url'], self.parse_novel_page, 
                cb_kwargs=dict(data=current_novel))
            # yield current_novel

        # next page
        next_page = response.css('div#pageArea a:nth-child(3)::attr(href)').get()
        if len(current_page_list) >= 90:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

    def parse_novel_page(self, response, data):
        data['collectionCount'] = response.css('span[itemprop="collectedCount"]::text').get()
        # remove useless tag
        tag_name_list = response.css('div.smallreadbody a::text').getall()
        tag_href_list = response.css('div.smallreadbody a::attr(href)').getall()
        tag_dict = {
            tag_name_list[i]: tag_href_list[i] for i in range(len(tag_name_list))
        }
        tag_remove_list = []
        for i in tag_dict.keys():
            if '?bq=' not in tag_dict[i] or len(i) > 4:
                tag_remove_list.append(i)
        for i in tag_remove_list:
            tag_dict.pop(i)
        data['tags'] = [i.strip() for i in tag_dict.keys() if len(i.strip()) > 0]
        data['cover'] = response.css('img.noveldefaultimage::attr(src)').get()
        data['searchKeyword'] = response.css('div.smallreadbody span.bluetext::text').get()
        yield data


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
            