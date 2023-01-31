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
  # 'Cookie': '__yjs_duid=1_77cfce1340baeafead6a4a2f055b930e1670412444002; smidV2=202103031715064a979117c753de178df22b237e6c183f00d561dfa9c942740; token=MTMzOTQwNjN8MjVmNTU3YzYzMTkyODRlODMzMDk1NzIzZWUyYzE5ZDR8fDk2MyoqKioqKkBxcS5jb218fDI1OTIwMDB8MXx8fOaZi%2Baxn%2BeUqOaIt3wxfG1vYmlsZXwxfDB8fA%3D%3D; testcookie=yes; timeOffset_o=-3541.89990234375; Hm_lvt_bc3b748c21fe5cf393d26c12b2c38d99=1672631103,1673157949,1674883377,1675140048; Hm_lpvt_bc3b748c21fe5cf393d26c12b2c38d99=1675140115; JJEVER=%7B%22fenzhan%22%3A%22yq%22%2C%22nicknameAndsign%22%3A%222%257E%2529%2524%25E5%258C%2597%25E6%2588%258A%22%2C%22sms_total%22%3A%220%22%2C%22desid%22%3A%22yMgIvzjrw07YjmSgmKc5Z+uhkooKDXGm%22%2C%22user_signin_days%22%3A%2220210816_13394063_0%22%2C%22foreverreader%22%3A%2213394063%22%2C%22background%22%3A%22%22%2C%22font_size%22%3A%22%22%2C%22isKindle%22%3A%22%22%2C%22lastCheckLoginTimePc%22%3A1675140129%2C%22shumeideviceId%22%3A%22WC39ZUyXRgdFIpTgzjXi1ZUJNGTQL0VXAGvh8GLNY+Lz8pWYRu2vOv4rgybiHOlMIqDqvrOQI3UpXZtfVp3n25bDEO7Vwt51PtL/WmrP2Tav+DYF2YqyHqwOOWjJRVZPLg4Wv483+KnQDHCzryoQD9qOLFH8bcaxN60aOyRtn/KdDSPJl+/5m8XER2+gB/bOwuWy7SN9djLYKGa3GpO86g7vmMUoqROS+mH9iT2SSW/sIq7GEpXWZnWOvXQ1EwrbmKQNUBns6fKQ%3D1487577677129%22%7D; arp_scroll_position=1624',
  # po18
  # 'Cookie': 'cross-site-cookie=name; PHPSESSID=c57e3256d736fe7bb2e69c2a9d5b84ab; nick=zhufree; password=b78644f90519eeb3358c2b53784bc03a; myname=youzi; lang=gb; Charm=0; Prestige=0; nickname=EB20190825192254647030; addvaluemoney=0; TSCvalue=gb; _gid=GA1.2.1302231141.1672631378; _gat_gtag_UA_71598951_1=1; _ga_WPJXT14CWH=GS1.1.1672631378.1.0.1672631378.0.0.0; _ga=GA1.1.102102717.1672631378',
  # haitang
  'Cookie': 'myname=youzi; lang=gb; Charm=0; Prestige=0; nickname=EB20190825192254647030; addvaluemoney=0; TSCvalue=gb; _ga_WPJXT14CWH=GS1.1.1672631378.1.1.1672631397.0.0.0; _ga=GA1.1.102102717.1672631378; cross-site-cookie=name',
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
