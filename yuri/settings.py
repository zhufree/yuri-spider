# Scrapy settings for jjyuri project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'yuri'

SPIDER_MODULES = ['yuri.spiders']
NEWSPIDER_MODULE = 'yuri.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'jjyuri (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 1
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 1
#CONCURRENT_REQUESTS_PER_IP = 1

# Disable cookies (enabled by default)
COOKIES_ENABLED = False
COOKIES_DEBUG = True
# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  # jjwxc
  # 'Cookie': '__yjs_duid=1_0d77b5fcf367ab0fc8bc5480456519121622557201139; smidV2=20210601222035f55cc93c348af50281869048e1f4538500e74138f6c2bd820; UM_distinctid=17d9f174b24495-068d6b634f88d3-57b1a33-144000-17d9f174b25cc2; CNZZDATA30075907=cnzz_eid%3D759150034-1622556863-%26ntime%3D1648110190; testcookie=yes; timeOffset_o=-1693.5; Hm_lvt_bc3b748c21fe5cf393d26c12b2c38d99=1648116832; JJSESS=%7B%22sidkey%22%3A%22Ed1S7qnFPGr8Aw3m6kTo9a0h4OvtcR5xljg%22%7D; token=MTMzOTQwNjN8OGUyNGFjZWNkMjhlOWFkZDNmNWIyNjdhNTM3YWFkYTB8fDk2MyoqKioqKkBxcS5jb218fDI1OTIwMDB8MXx8fOaZi%2Baxn%2BeUqOaIt3wxfG1vYmlsZXwx; JJEVER=%7B%22fenzhan%22%3A%22dm%22%2C%22nicknameAndsign%22%3A%222%257E%2529%2524%25E5%258C%2597%25E6%2588%258A%22%2C%22foreverreader%22%3A%2213394063%22%2C%22desid%22%3A%22kajd9flfnGOj4ki6IU8/mJ7Cuo5Pwysf%22%2C%22sms_total%22%3A1%2C%22user_signin_days%22%3A%2220210917_13394063_0%22%2C%22lastCheckLoginTimePc%22%3A%221644847754%22%2C%22background%22%3A%22%22%2C%22font_size%22%3A%22%22%2C%22isKindle%22%3A%22%22%7D; Hm_lpvt_bc3b748c21fe5cf393d26c12b2c38d99=1648116870',
  # po18
  # 'Cookie': '_ga=GA1.2.1006285981.1648649084; authtoken1=emh1ZnJlZQ%3D%3D; authtoken6=1; bgcolor=bg-default; word=select-m; _paabbcc=irkgfcg0o7v4o9dschbfujj8n5; _po18rf-tk001=afcc828d905bbabe6690d48cdd13ff1d67f78f0e8fced015b1784d3706b7da58a%3A2%3A%7Bi%3A0%3Bs%3A13%3A%22_po18rf-tk001%22%3Bi%3A1%3Bs%3A32%3A%22AgQQpJ7dGhFDvHB3LfeXmv1oOrV3qNfs%22%3B%7D; _gid=GA1.2.1601527305.1652156132; _gat_gtag_UA_11633339_26=1; po18Limit=1; _gat_gtag_UA_11633339_27=1; url=https%3A%2F%2Fwww.po18.tw; authtoken2=YTk5MGM3YzVkNDAzMzZlZTNiZTAyMjE0NzAzMjlmNDg%3D; authtoken3=1821092935; authtoken4=3035287360; authtoken5=1652156144',
  # haitang
  'Cookie': 'TSCvalue=gb; _gid=GA1.2.489008424.1655219736; pjAcceptCookie=YES; cross-site-cookie=name; PHPSESSID=65dc0e8ec6aedec730d98ba49ff7335d; nick=zhufree; password=b78644f90519eeb3358c2b53784bc03a; myname=youzi; lang=gb; Charm=0; Prestige=0; nickname=EB20190825192254647030; addvaluemoney=0; nowviewbookid=118691; alsoviewbookid=118691; _ga_WPJXT14CWH=GS1.1.1655257778.2.1.1655259113.0; _ga=GA1.2.2056089295.1655219735',
  # blank
  #'Cookie': '',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
# DEFAULT_REQUEST_HEADERS = {}
# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'jjyuri.middlewares.JjyuriSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'jjyuri.middlewares.JjyuriDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'yuri.pipelines.YuriPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
