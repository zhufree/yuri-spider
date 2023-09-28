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
  # 'Cookie': 'smidV2=202103031715064a979117c753de178df22b237e6c183f00d561dfa9c942740; __yjs_duid=1_9d76c99bf888ff61477b115b6329fb0f1680783741886; Hm_lvt_bc3b748c21fe5cf393d26c12b2c38d99=1691764232; bbsnicknameAndsign=2%257E%2529%2524%25E5%258C%2597%25E6%2588%258A; testcookie=yes; timeOffset_o=-1534.5; token=MTMzOTQwNjN8Y2M2MTUyZTY2M2E5ZDQzMTBkMmVhYzVjYjM2MjZkN2V8fDk2MyoqKioqKkBxcS5jb218fDI1OTIwMDB8MXx8fOaZi%2Baxn%2BeUqOaIt3wxfG1vYmlsZXwxfDB8fA%3D%3D; JJEVER=%7B%22fenzhan%22%3A%22yq%22%2C%22nicknameAndsign%22%3A%222%257E%2529%2524%25E5%258C%2597%25E6%2588%258A%22%2C%22sms_total%22%3A%220%22%2C%22desid%22%3A%22woaFZFYmhUgbCwBt3AHfdg8ZQ7bMORXB%22%2C%22user_signin_days%22%3A%2220210816_13394063_0%22%2C%22foreverreader%22%3A%2213394063%22%2C%22background%22%3A%22%22%2C%22font_size%22%3A%22%22%2C%22isKindle%22%3A%22%22%2C%22lastCheckLoginTimePc%22%3A%221695176432%22%2C%22shumeideviceId%22%3A%22WC39ZUyXRgdFIpTgzjXi1ZUJNGTQL0VXAGvh8GLNY%2BLz8pWYRu2vOv4rgybiHOlMIqDqvrOQI3UpXZtfVp3n25bDEO7Vwt51PtL%5C%2FWmrP2Tav%2BDYF2YqyHq11RBXoT3lNe3fVLMpg6KnLRSiimUmMxhJ4mCbdPQ1BRajW7hxiYtqOGduzx9VSOoUCqgMwPBHjV0JSgM%5C%2FvzIa0G7wWr0zokq6ygVTmYmOcCtuyX%5C%2FAM2MBOa224ILWvDXsYnknGcImw52eDSNFSlDac%3D1487577677129%22%7D; JJSESS=%7B%22returnUrl%22%3A%22https%3A//www.jjwxc.net/bookbase.php%3Fxx3%3D3%26sortType%3D3%22%2C%22sidkey%22%3A%22Iux0DgTSColvKqFkZJ78smHzc9XPtBO%22%2C%22clicktype%22%3A%22%22%7D; bbstoken=MTMzOTQwNjNfMF83NjIwOWU0NjlmYmU0N2EzZGM3MDgxMTM2ZGUzMWJiZF8xX19fMQ%3D%3D',
  # po18
  'Cookie': '_paabbcc=bml78hp72u9l1rlf4vuasaa7u5; _po18rf-tk001=f6eb1c48350489db6d6e965aca2dba10eda69fc61c651a33061a53f86b370931a%3A2%3A%7Bi%3A0%3Bs%3A13%3A%22_po18rf-tk001%22%3Bi%3A1%3Bs%3A32%3A%22UWLOwnZKqiCZs_5VbrRm0Vu-RjAKKWro%22%3B%7D; po18Limit=1',
  # haitang
  # 'Cookie': 'PHPSESSID=2087238d229202c73ae3615f33eb6512; cross-site-cookie=name; nick=zhufree; password=b78644f90519eeb3358c2b53784bc03a; myname=youzi; lang=gb; Charm=0; Prestige=0; nickname=EB20190825192254647030; addvaluemoney=0; TSCvalue=gb; pjAcceptCookie=YES',
  #NU
  # 'Cookie': '__unid=4fc83abe-39d6-cad5-0bb2-ff6494265794; _lr_env_src_ats=false; wordpress_logged_in_6beec58f7168d95c44933bfb0d113ee4=zhufree%7C1694508414%7CC9ZjR3NQknep2afE2Ei8VKzXqGxQiyeVWDstRw8MB83%7Cf0515d2271c2bc9e858f92eeae1ffb39096da772920be38e19b4da12db920d58; euconsent-v2=CPpiogAPpiogABEACBENC9CoAP_AAH_AAAIwJStf_X__b3_v-_7___t0eY1f9_7__-0zjhfdt-8N3f_X_L8X_2M7vF36tr4KuR4ku3bBIUdtHPncTVmx6olVrzPsbk2cr7NKJ_Pkmnsbe2dYGH9_n9_z_ZKZ7___f__7________________________3______________________________________________-4JStf_X__b3_v-_7___t0eY1f9_7__-0zjhfdt-8N3f_X_L8X_2M7vF36tr4KuR4ku3bBIUdtHPncTVmx6olVrzPsbk2cr7NKJ_Pkmnsbe2dYGH9_n9_z_ZKZ7___f__7________________________3______________________________________________-4AA; _ga=GA1.2.1984547997.1682732298; pbjs-unifiedid=%7B%22TDID%22%3A%22d6409d7a-9b7b-4e73-9123-b9653bab6a12%22%2C%22TDID_LOOKUP%22%3A%22TRUE%22%2C%22TDID_CREATED_AT%22%3A%222023-03-29T01%3A38%3A18%22%7D; _cc_id=66947cf367079d3bb47e59ae405796d3; __gads=ID=b329119a4d1444b0:T=1682732300:S=ALNI_MbvmhuXi-G5nxhX0dyQkatK2OOqaQ; _pbjs_userid_consent_data=6683316680106290; unic-consent=BPrzpwAPrzpwA8AAAA; rankgraph=0,0,0,1,1; __gpi=UID=00000bff2c63abd1:T=1682732300:RT=1684810945:S=ALNI_MbZaoN1M7BQWmcFVkbOU0Nhd4KDWQ; sort_rev=datenew; cto_bundle=gFHfil9kZFRhYXVucWRTZSUyQll4YVJlS0NTMzJwODhhVnpkd3RTNmYwbzYycHdJJTJGcCUyQjJQUXVESUY1akpqNjBCMDZKQnZaNXdONGx2TVlQNWdNaXBZeE5TSmR0cCUyQk9EY2UlMkZVRTJBcWYzUHByRlQ2T2Z5ZSUyRmZqVlFMRHdkVTEwOFN2aFYyU1Y3SUxnUDUyJTJCTEFEbGs4TzliNkJKcndtdVdSS0xiUnBlRE54UG9CVXdJbyUzRA; cto_bidid=X1ZQRl9UM25OV0FNJTJCMXB3MHJlRmhYJTJGV2ExRWQlMkJZNW5kR3AlMkY4TnhnYm9VZ2dhRXZXU3M1WVFWRnBYSjNUaDgzclhUVWNTUHJUMXF4VWRxNTVTJTJGM05YV2VaZUd0ZkxtOGJoeXFObm1EeHp6cGxGRWl5Smc4N3JVeUJFYXVCVGhrakNpMnc; cf_clearance=7JeMBfQs5D3uGuGgHLFt2ttE52YWNihPsmwAX_Vxt1g-1684896405-0-250; sharedid=a277e0cd-7386-41bc-b75d-b8e471ab4998; _lr_retry_request=true',
  # blank
  # 'Cookie': '',
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
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
