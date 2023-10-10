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
  # 'Cookie': '_paabbcc=bml78hp72u9l1rlf4vuasaa7u5; _po18rf-tk001=f6eb1c48350489db6d6e965aca2dba10eda69fc61c651a33061a53f86b370931a%3A2%3A%7Bi%3A0%3Bs%3A13%3A%22_po18rf-tk001%22%3Bi%3A1%3Bs%3A32%3A%22UWLOwnZKqiCZs_5VbrRm0Vu-RjAKKWro%22%3B%7D; po18Limit=1',
  # haitang
  # 'Cookie': 'PHPSESSID=2087238d229202c73ae3615f33eb6512; cross-site-cookie=name; nick=zhufree; password=b78644f90519eeb3358c2b53784bc03a; myname=youzi; lang=gb; Charm=0; Prestige=0; nickname=EB20190825192254647030; addvaluemoney=0; TSCvalue=gb; pjAcceptCookie=YES',
  #NU
  # 'Cookie': '_cc_id=a6d7da13d4be872e47dff39deed049ee; __utma=37109695.7336321.1668166472.1678712069.1679053515.5; _pbjs_userid_consent_data=6683316680106290; _lr_env_src_ats=false; _au_1d=AU1D-0100-001689568806-RNRQ8IC2-IT8K; sharedid=38d0f4ef-7bfd-48bb-98f1-4e698dcf9eca; wordpress_logged_in_6beec58f7168d95c44933bfb0d113ee4=zhufree%7C1709432232%7COINSMSmTx3MhQvOMIXjoPUXSJLXQVHacrLkOxlg5Eeu%7Cbfe29a03dd8f5039a15b0801d37eb2863d9b669fe882e50cd84911a387ea28a9; __unid=a4776dcb-6b57-2a55-c823-069443996d00; connectId={"lastUsed":1694225401470,"lastSynced":1694225401470}; __gads=ID=1a34014683ac76a7:T=1668166478:RT=1694691778:S=ALNI_MbANVgIinNpywO_vVulw4O9SxOKkA; __gpi=UID=00000b79f852cc15:T=1668166478:RT=1694691778:S=ALNI_MZdLWXh4ZMGkq5ITvi0Gnmj61Az_A; unic-consent=BPyFwIAPyFwIA8AAAA; _au_last_seen_pixels=eyJhcG4iOjE2OTQ2OTE3ODIsInR0ZCI6MTY5NDY5MTc4MiwicHViIjoxNjk0NjkxNzgyLCJydWIiOjE2OTQ2OTE3ODIsInRhcGFkIjoxNjk0NjkxNzgyLCJhZHgiOjE2OTQ2OTE3ODIsImdvbyI6MTY5NDY5MTc4MiwiYWRvIjoxNjk0NjkxODQ5LCJ1bnJ1bHkiOjE2OTQ2OTE4NDksInNtYXJ0IjoxNjk0NjkxODQ5LCJ0YWJvb2xhIjoxNjk0NjkxNzgyLCJzb24iOjE2OTQ2OTE4NDksInBwbnQiOjE2OTQ2OTE3ODIsImltcHIiOjE2OTQ2OTE4NDksImNvbG9zc3VzIjoxNjk0NjkxODQ5LCJvcGVueCI6MTY5NDY5MTg0OSwiYmVlcyI6MTY5NDY5MTg0OSwiYW1vIjoxNjk0NjkxODQ5LCJpbmRleCI6MTY5NDY5MTc4Mn0%3D; cto_bundle=c7Y3z194ZHJzNlB6T2lnT2xydk1sQlRIanZqWWhreGYxWmhIaU9NSDlPeTRmdXNBazYlMkYxa3ZxM0pLZmlDcFpMNGQxVVZPV25mUDVIdUVKd1ExSHZGb1klMkZOSmpkV0FnczFEJTJGdW0wZGQlMkJGajVBQnZjVVpxU2xYT3ozdXZrTWJ4cTRtdG1hY2QxU0xtd244ZmZyamE5RDI3WiUyQnlRJTNEJTNE; cto_bidid=XkildF9NeFdKJTJCUEpYcjJjOHhnakY1YyUyQm02bFhsZ2J1Qkl5JTJCcjBobUtFaXNNNkpiUDQlMkY2OGZ4Sm9MbWNkR2pxYzRldWZqekc2OTJuZWNpcExVWW9RNG1IYjVrM0dyYzBwJTJGY1RvOHZNa3doQWhiNVdVVHZVN1ljVHlsMlprSHN4WkZEejU; _ga=GA1.1.7336321.1668166472; euconsent-v2=CPzBFAAPzBFAABEACBENDXCoAP_AAH_AAAIwgoNf_X__b3_v-_7___t0eY1f9_7__-0zjhfdt-8N3f_X_L8X_2M7vF36tr4KuR4ku3bBIUdtHPncTVmx6olVrzPsbk2cr7NKJ_Pkmnsbe2dYGH9_n9_z_ZKZ7___f__7_______________________________________________________________________-_______2AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAARBQa_-v_-3v_f9_3___bo8xq_7_3__9pnHC-7b94bu_-v-X4v_sZ3eLv1bXwVcjxJdu2CQo7aOfO4mrNj1RKrXmfY3Js5X2aUT-fJNPY29s6wMP7_P7_n-yUz3__-___3_______________________________________________________________________9_______sAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAA; _ga_99KSGKVVYB=GS1.1.1696217053.9.1.1696217649.60.0.0; cf_clearance=O18ZDokbIiXu3oDgVQYwj47puwPz4.7YMYR1o584RjE-1696310151-0-1-bb4cef42.3ca49ac9.ec4db0a2-250.2.1696310151; sharedid_cst=TyylLI8srA%3D%3D; panoramaId_expiry=1696914954108; panoramaId=b692b20900cc7664b6c390ebf6c216d539385ee89e6f84d9606d7af505a1111b',
  # blank
  # 'Cookie': '',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
}
# DEFAULT_REQUEST_HEADERS = {}
# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'jjyuri.middlewares.JjyuriSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'yuri.middlewares.DebugCookiesMiddleware': 543,
}

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
