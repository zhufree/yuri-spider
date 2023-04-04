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
  # 'Cookie': 'timeOffset_o=-1553.39990234375; translate_table_struct=left_right; __yjs_duid=1_080d6d5ef5414bda956735a9b81b13aa1679362355524; smidV2=20230321093236f8078f589a6a0e7a5ed3fdff7af088bb00eba86736a4f0b70; token=MTMzOTQwNjN8NDA1NGE2NzEwOGRiNmI3NWM1OGRmZjRiNGVkY2Y1Y2F8fDk2MyoqKioqKkBxcS5jb218fDI1OTIwMDB8MXx8fOaZi%2Baxn%2BeUqOaIt3wxfG1vYmlsZXwxfDB8fA%3D%3D; bbsnicknameAndsign=2%257E%2529%2524%25E5%258C%2597%25E6%2588%258A; bbstoken=MTMzOTQwNjNfMF80OGJhZjI0ZWU5OThmZGIyOGVkOWMzNDQwZDE0N2Q5Nl8xX19fMQ%3D%3D; testcookie=yes; JJSESS=%7B%22clicktype%22%3A%22%22%7D; timeOffset_o=-600.300048828125; JJEVER=%7B%22shumeideviceId%22%3A%22WC39ZUyXRgdEgkRee+u/BMHDZenrzbDzn9C8AxdRre5Y9DIIUIOm645jVmahmZIIJdt/s58iKEAiApNPAesfYLNlW4XB7Qwa9tL/WmrP2Tav+DYF2YqyHqw2IpW7gjNTa3fVLMpg6KnK+4M2GQH+t5J4mCbdPQ1BRajW7hxiYtqOGduzx9VSOoSmy3UdJX7LX0JSgM/vzIa0G7wWr0zokqzQmFsHr/mDW+c+Cbjf7v6jlDggBrgwYaKcmJ+vYB79M1487577677129%22%2C%22nicknameAndsign%22%3A%222%257E%2529%2524%25E5%258C%2597%25E6%2588%258A%22%2C%22foreverreader%22%3A%2213394063%22%2C%22desid%22%3A%22ThAcNI3+k8yQ4y3afepGknnRz89y0VCU%22%2C%22sms_total%22%3A0%2C%22lastCheckLoginTimePc%22%3A1680506517%7D',
  # po18
  # 'Cookie': 'cross-site-cookie=name; PHPSESSID=c57e3256d736fe7bb2e69c2a9d5b84ab; nick=zhufree; password=b78644f90519eeb3358c2b53784bc03a; myname=youzi; lang=gb; Charm=0; Prestige=0; nickname=EB20190825192254647030; addvaluemoney=0; TSCvalue=gb; _gid=GA1.2.1302231141.1672631378; _gat_gtag_UA_71598951_1=1; _ga_WPJXT14CWH=GS1.1.1672631378.1.0.1672631378.0.0.0; _ga=GA1.1.102102717.1672631378',
  # haitang
  'Cookie': 'cross-site-cookie=name; TSCvalue=gb; PHPSESSID=dc750a30d49658dde2cd1dc880c6bcd1; nick=zhufree; password=b78644f90519eeb3358c2b53784bc03a; myname=youzi; lang=gb; Charm=0; Prestige=0; nickname=EB20190825192254647030; addvaluemoney=0',
  # blank
  # 'Cookie': '',
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
