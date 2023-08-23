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
  # 'Cookie': '__yjs_duid=1_c16d402cb6e54ab6eef682db05a237c51692502178945; testcookie=yes; smidV2=202308201129396e60d754baa4ba4489411c799defa193001c0be1e4b772140; timeOffset_o=-1049.699951171875; token=MTMzOTQwNjN8NTFiZTM4YWEyNGQ0MjJkODU4N2FhNmQyY2QwY2E5OTh8fDk2MyoqKioqKkBxcS5jb218fDI1OTIwMDB8MXx8fOaZi%2Baxn%2BeUqOaIt3wxfG1vYmlsZXwxfDB8fA%3D%3D; JJEVER=%7B%22shumeideviceId%22%3A%22WC39ZUyXRgdHOMjWQwzjLmmRxoRMoSO9gyuvGSnkHym0sWPX4gKcNkH54G7j1xgbQuY8c%2B2qonLRX2%2BQznk0N8FHhZMTXGe%5C%2F4tL%5C%2FWmrP2Tav%2BDYF2YqyHq3%5C%2Ff%2BEaCua5r3fVLMpg6KnK%2B4M2GQH%2Bt5J4mCbdPQ1BRajW7hxiYtqOGduzx9VSOoT%2BachOlAQdn0JSgM%5C%2FvzIa0G7wWr0zokq66IbTCLWylNJZ%5C%2FWkAAhqS%2BVcCjCjQzA2poQMnY11jut1487577677129%22%2C%22nicknameAndsign%22%3A%222%257E%2529%2524%25E5%258C%2597%25E6%2588%258A%22%2C%22foreverreader%22%3A%2213394063%22%2C%22desid%22%3A%225mdituiUCWrT%5C%2FZa9%2Bv5ROkkD8kZrrdD7%22%7D; JJSESS=%7B%22clicktype%22%3A%22%22%2C%22returnUrl%22%3A%22https%3A//www.jjwxc.net/onebook.php%3Fnovelid%3D8166683%22%2C%22sidkey%22%3A%22w0BFCmtnS3df92LDg6E5qAcZQG17kYWuU%22%7D',
  # po18
  'Cookie': '_paabbcc=e79rk45p9bjelbmohm3d9353e7; _po18rf-tk001=b114a4492d55c69ac030c969327a9f00856c60c259d9af9446799b15c130ba12a%3A2%3A%7Bi%3A0%3Bs%3A13%3A%22_po18rf-tk001%22%3Bi%3A1%3Bs%3A32%3A%225YFNvokjFwcUsQUPh1aRFQ0CXYhl-gXt%22%3B%7D; po18Limit=1; url=https%3A%2F%2Fwww.po18.tw; authtoken1=emh1ZnJlZQ%3D%3D; authtoken2=ZjBhZjRjNjJmNzdjYjQ0MWQ3YmRmMmMxYzUwOTU2OTU%3D; authtoken3=1821092935; authtoken4=1185428703; authtoken5=1692709091; authtoken6=1',
  # haitang
  # 'Cookie': 'TSCvalue=gb; cross-site-cookie=name; PHPSESSID=a5c5335143395e0292027643ae8d8ae4; nick=zhufree; password=b78644f90519eeb3358c2b53784bc03a; myname=youzi; lang=gb; Charm=0; Prestige=0; nickname=EB20190825192254647030; addvaluemoney=0',
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
