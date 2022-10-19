import scrapy
from pyquery import PyQuery as pq
from pyunit_time import Time
import time, re, json

# last update at 9.8
class YuriSpider(scrapy.Spider):
    name = "jjwxc"

    start_urls = [
        # 'http://www.jjwxc.net/bookbase.php?xx3=3',
        'https://www.jjwxc.net/bookbase.php?xx3=3&sortType=3' # 按发表时间
        # 'https://www.jjwxc.net/bookbase.php?xx3=3&sortType=3&page=400' # 500 开始大概是2020年的作品
    ]
    page_count = 0

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
            if '完' in current_novel['status']:
                current_novel['status'] = '完结'
            elif current_novel['status'] == '暂停':
                current_novel['status'] = '断更'
            elif current_novel['status'] == '连载中':
                current_novel['status'] = '连载'
            current_novel['bid'] = 'jj' + current_novel['book_url'].split('=')[-1]
            current_novel['aid'] = 'jj' + current_novel['author_url'].split('=')[-1]
            current_page_list.append(current_novel)
            # open novel page for more info
            yield scrapy.Request(current_novel['book_url'], self.parse_novel_page, 
                cb_kwargs=dict(data=current_novel))
            # yield current_novel

        # next page
        next_page = response.css('div#pageArea a:nth-child(3)::attr(href)').get()
        if len(current_page_list) >= 60 and self.page_count < 30: # 根据时间修改page count
            next_page = response.urljoin(next_page)
            self.page_count += 1
            yield scrapy.Request(next_page, callback=self.parse)

    def parse_novel_page(self, response, data):
        collection_count = response.css('span[itemprop="collectedCount"]::text').get()
        if collection_count != None:
            data['collectionCount'] = collection_count
        else:
            data['collectionCount'] = '0'
        desc = response.css('div[itemprop="description"]::text').get()
        data['description'] = desc if desc != None else ''
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
        cover = response.css('img.noveldefaultimage::attr(src)').get()
        data['cover'] = cover if cover != None else ''
        keyword = response.css('div.smallreadbody span.bluetext::text').get()
        data['searchKeyword'] = keyword if keyword != None else ''
        yield data

class HaitangSpider(scrapy.Spider):
    name = 'haitang'
    allowed_domains = ['www.newhtbook.com']
    start_urls = ['https://www.newhtbook.com/searchlist.php?fixlangsnd=FsedAjjT6&fixlangact=edit&selsexytype=c']
    # start_urls = ['http://ebook.longmabook.com/searchlist.php?fixlangsnd=FsedAjjT6&fixlangact=edit&selsexytype=c']
    # &searchkpage=2

    def __init__(self):
        self.page_count = 1
        self.base_url = 'https://www.newhtbook.com/searchlist.php?fixlangsnd=FsedAjjT6&fixlangact=edit&selsexytype=c'
        # self.base_url = 'http://ebook.longmabook.com/searchlist.php?fixlangsnd=FsedAjjT6&fixlangact=edit&selsexytype=c'

    def parse(self, response):
        tds = response.css('table.uk-table tr>td')[1:]
        for td in tds:
            href = td.css('a:first-child::attr(href)').get()
            item = {
                'title': td.css('a:first-child>font>b::text').get(),
                'book_url': 'https://www.newhtbook.com' + href,
                # 'book_url': 'http://ebook.longmabook.com' + href,
                'bid': 'ht' + re.search(r'bookid=(\d+)', href).group(1),
                'author': td.css('a:nth-child(6)>font::text').get(),
                'author_url': 'https://www.newhtbook.com' + td.css('a:nth-child(6)::attr(href)').get(),
                'tags': [i.strip() for i in td.css('font:nth-child(4)::text').get().split('/')],
                'status': td.css('font:nth-child(8)::text').get(),
                'wordcount': td.css('font:nth-child(9)::text').get(),
                'cover': 'https://s.pc.qq.com/tousu/img/20211109/6818272_1636439546.jpg',
                'style': '',
                'type': '',
                'publish_time': '',
                'searchKeyword': '',
                'description': ''
            }
            item['tags'] = list(set(item['tags']))
            item['aid'] = item['author_url'].split('=')[-1]
            
            if item['wordcount'] == None:
                item['wordcount'] = 0
            else:
                w = re.search(r'約(\d+)萬字', item['wordcount'])
                if w == None:
                    item['wordcount'] = int(re.search(r'約(\d+)字', item['wordcount']).group(1))
                else:
                    item['wordcount'] = int(w.group(1)) * 10000
            if item['wordcount'] == None:
                item['wordcount'] = 0

            yield scrapy.Request(item['book_url'], self.parse_detail, 
                cb_kwargs=dict(data=item))

        if len(tds) >= 50 and self.page_count < 5: # 根据时间修改page count
            self.page_count += 1
            next_page = self.base_url + '&searchkpage={}'.format(self.page_count)
            yield scrapy.Request(next_page, callback=self.parse)

    def parse_detail(self, response, data):
        collection_count_el = response.css('div.uk-card font:nth-child(8)::text').get()
        if collection_count_el == None:
            collection_count_el = response.css('div.uk-card font:nth-child(7)::text').get()
        data['collectionCount'] = collection_count_el

        # description
        td_content = response.css('div.uk-card').get()
        td_content = td_content.replace('<br>', '')
        desc_search = re.search(r'<font color="#800080".*</font>(.*?)<div id=', td_content, flags=re.DOTALL)
        if desc_search != None:
            data['description'] = desc_search.group(1).strip()
        
        # open list page to get publish time
        list_url = 'https://www.newhtbook.com/showbooklist.php'
        # list_url = 'http://ebook.longmabook.com/showbooklist.php'
        post_data = {
          'ebookid': data['bid'][2:], 
          'showbooklisttype': '1'
        }
        yield scrapy.FormRequest(list_url, self.parse_list, formdata=post_data, 
                cb_kwargs=dict(data=data))
    
    def parse_list(self, response, data):
        time_search = re.search(r'uk-tooltip="刊登時間"></span></font>(.*?)&nbsp;', response.text)
        if time_search != None:
            data['publish_time'] = time_search.group(1)
        yield data

# 默认只抓前100条
class CpSpider(scrapy.Spider):
    name = 'changpei'
    allowed_domains = ['gongzicp.com']
    start_urls = ['https://webapi.gongzicp.com/novel/novelGetList?page=1&tid=17&order=-1&field=4'] # 创建时间，最新
    handle_httpstatus_list = [404]  # 处理404页面，否则将会跳过
    
    def __init__(self):
        self.page_count = 1
        self.base_url = 'https://webapi.gongzicp.com/novel/novelGetList?page={}&tid=17&order=-1&field=4'
        self.current_year = str(time.localtime().tm_year)
        self.current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    def parse(self, response):
        res_json = response.json()
        novel_list = res_json['data']['list']
        for j in novel_list:
            current_novel = {
                'title': j['novel_name'],
                'bid': 'cp' + str(j['novel_id']),
                'book_url': 'https://www.gongzicp.com/novel-{}.html'.format(j['novel_id']),
                'aid': 'cp' + str(j['author_id']),
                'author': j['novel_author'],
                'author_url': 'https://www.gongzicp.com/zone/author-{}.html'.format(j['author_id']),
                'style': '',
                'type': j['type_name'],
                'publish_time': j['novel_uptime'],
                'status': j['novel_process_text'],
                'cover': j['novel_cover'],
                'wordcount': str(j['novel_wordnumber']).replace(',', ''),
                'tags': j['novel_tags'],
                'searchKeyword': j['novel_desc'],
                'description': ''
            }
            if not '-' in current_novel['publish_time']:
                parse_result = Time(self.current_time).parse(current_novel['publish_time'])
                if len(parse_result) > 0:
                    current_novel['publish_time'] = parse_result[0]['keyDate']
            if len(current_novel['publish_time']) < 6:
                current_novel['publish_time'] = self.current_year + '-' + current_novel['publish_time']
            book_api = 'https://webapi.gongzicp.com/novel/novelGetInfo?id={}'.format(j['novel_id'])
            time.sleep(0.5)
            yield scrapy.Request(book_api, self.parse_novel_page, 
                cb_kwargs=dict(data=current_novel))
            
        if len(novel_list) == 10 and self.page_count < 10: # 前100条
            self.page_count += 1
            next_page = self.base_url.format(self.page_count)
            time.sleep(0.5)
            yield scrapy.Request(next_page, callback=self.parse)

    def parse_novel_page(self, response, data):
        if response.status == 404:
            data['collectionCount'] = -1
            yield data
        else:
            res_json = response.json()
            novel_info = res_json['data']['novelInfo']
            if type(novel_info) == list:
                data['collectionCount'] = -1
                yield data
            else:
                data['type'] = novel_info['type_names']
                data['collectionCount'] = novel_info['novel_allcoll'] if novel_info['novel_allcoll'] != None else -1
                data['publish_time']= novel_info['create_time']
                data['description'] = novel_info['novel_info']
                yield data

class PoSpider(scrapy.Spider):
    name = 'po'
    allowed_domains = ['www.po18.tw']
    start_urls = ['https://www.po18.tw/tags/subbooks?id=23_'] #按最新章回的更新时间排序的

    def __init__(self):
        self.page_count = 1
        self.base_url = 'https://www.po18.tw/tags/subbooks?id=23_'

    def parse(self, response):
        divs = response.css('#w0.list-view>div')
        for div in divs:
            href = div.css('.book_name>a::attr(href)').get()
            item = {
                'title': div.css('.book_name>a::text').get(),
                'book_url': 'https://www.po18.tw' + href,
                'bid': 'po' + re.search(r'books/(\d+)', href).group(1),
                'author': div.css('.book_author>a::text').get(),
                'author_url': 'https://www.po18.tw' + div.css('.book_author>a::attr(href)').get(),
                'tags': [i.strip() for i in div.css('.book_tags>a.tag::text').getall()],
                'cover': div.css('.book_cover img::attr(src)').get(),
                'style': '',
                'type': '',
                'publish_time': '',
                'description': '',
                'searchKeyword': div.css('.intro::text').get()
            }
            item['tags'] = list(set(item['tags']))
            item['aid'] = 'po' + item['author_url'].replace('https://www.po18.tw/users/', '')

            yield scrapy.Request(item['book_url'], callback=self.parse_detail, meta={'dont_redirect': True,'handle_httpstatus_list': [302]}, 
                cb_kwargs=dict(data=item))

        if len(divs) >= 10 and self.page_count < 3:
            self.page_count += 1
            next_page = self.base_url + '&page={}'.format(self.page_count)
            yield scrapy.Request(next_page, callback=self.parse)

    def parse_detail(self, response, data):
        data['description'] = response.css('.B_I_content').get()
        data['status'] = response.css('dd.statu::text').get()
        data['wordcount'] = response.css('table.book_data>tbody>tr:nth-child(3)>td::text').get()
        data['collectionCount'] = response.css('table.book_data:nth-child(2)>tbody>tr:nth-child(1)>td::text').get()
        
        article_list_url = f"https://www.po18.tw/books/{data['bid'][2:]}/articles"
        yield scrapy.Request(article_list_url, callback=self.parse_list, meta={'dont_redirect': True,'handle_httpstatus_list': [302]}, 
                cb_kwargs=dict(data=data))

    def parse_list(self, response, data):
        first_item = response.css('#w0.list-view>div:nth-child(1) .l_date::text').get()
        if first_item != None:
            data['publish_time'] = first_item.split(' ')[1]
        yield data
