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
  # 'Cookie': '__yjs_duid=1_080d6d5ef5414bda956735a9b81b13aa1679362355524; smidV2=20230321093236f8078f589a6a0e7a5ed3fdff7af088bb00eba86736a4f0b70; bbsnicknameAndsign=2%257E%2529%2524%25E5%258C%2597%25E6%2588%258A; token=MTMzOTQwNjN8OWRkYjA0NGFmODAzOTFiYThmMmUyYjM4ZjYxMDcyYmJ8fDk2MyoqKioqKkBxcS5jb218fDI1OTIwMDB8MXx8fOaZi%2Baxn%2BeUqOaIt3wxfG1vYmlsZXwxfDB8fA%3D%3D; bbstoken=MTMzOTQwNjNfMF8xYzY5ZDViZGY4NmJmNzk2ZmUzNjQyMzE2MTQ4N2IyNl8xX19fMQ%3D%3D; Hm_lvt_bc3b748c21fe5cf393d26c12b2c38d99=1680874957,1682314848; inviteid=169503662; testcookie=yes; timeOffset_o=-479.39990234375; JJEVER=%7B%22shumeideviceId%22%3A%22WC39ZUyXRgdEgkRee+u/BMHDZenrzbDzn9C8AxdRre5Y9DIIUIOm645jVmahmZIIJdt/s58iKEAiApNPAesfYLNlW4XB7Qwa9tL/WmrP2Tav+DYF2YqyHq6v5Q9CawY8H3fVLMpg6KnLRSiimUmMxhJ4mCbdPQ1BRajW7hxiYtqOGduzx9VSOocyVfqZBtj9v0JSgM/vzIa0G7wWr0zokqzb4z9Yh/BzR3wnHhnwknrvp6ldOz3cVBqcmJ+vYB79M1487577677129%22%2C%22nicknameAndsign%22%3A%222%257E%2529%2524%25E5%258C%2597%25E6%2588%258A%22%2C%22foreverreader%22%3A%2213394063%22%2C%22desid%22%3A%22XnTjqG2NFW1fGAxlETdLEZ1OsSa/s7cr%22%2C%22sms_total%22%3A%220%22%2C%22lastCheckLoginTimePc%22%3A1683249151%2C%22background%22%3A%22%22%2C%22font_size%22%3A%22%22%2C%22isKindle%22%3A%22%22%7D',
  # po18
  'Cookie': '_paabbcc=iakqrj16o54r28675cqkac9vu2; _po18rf-tk001=1e07865c6f245f04e09975dbf7767c447261031ec797e5026d17f228a6c5367ba%3A2%3A%7Bi%3A0%3Bs%3A13%3A%22_po18rf-tk001%22%3Bi%3A1%3Bs%3A32%3A%22ZDT2Qrut6BprvtDErC2x_z24s-RYflQq%22%3B%7D; po18Limit=1; url=https%3A%2F%2Fwww.po18.tw; authtoken1=emh1ZnJlZQ%3D%3D; authtoken2=OGRiNDUxZmJhZWI2NTJiZDUwMzE0ODgyMTk1MzM4Njg%3D; authtoken3=1821092935; authtoken4=3410067547; authtoken5=1683293943; authtoken6=1',
  # haitang
  # 'Cookie': 'TSCvalue=gb; cross-site-cookie=name; PHPSESSID=a5c5335143395e0292027643ae8d8ae4; nick=zhufree; password=b78644f90519eeb3358c2b53784bc03a; myname=youzi; lang=gb; Charm=0; Prestige=0; nickname=EB20190825192254647030; addvaluemoney=0',
  #NU
  # 'Cookie': '__unid=4fc83abe-39d6-cad5-0bb2-ff6494265794; sharedid=d7e1a0c0-eb3d-4cde-bfd9-1590b44c98f7; _lr_env_src_ats=false; wordpress_logged_in_6beec58f7168d95c44933bfb0d113ee4=zhufree%7C1694508414%7CC9ZjR3NQknep2afE2Ei8VKzXqGxQiyeVWDstRw8MB83%7Cf0515d2271c2bc9e858f92eeae1ffb39096da772920be38e19b4da12db920d58; euconsent-v2=CPpiogAPpiogABEACBENC9CoAP_AAH_AAAIwJStf_X__b3_v-_7___t0eY1f9_7__-0zjhfdt-8N3f_X_L8X_2M7vF36tr4KuR4ku3bBIUdtHPncTVmx6olVrzPsbk2cr7NKJ_Pkmnsbe2dYGH9_n9_z_ZKZ7___f__7________________________3______________________________________________-4JStf_X__b3_v-_7___t0eY1f9_7__-0zjhfdt-8N3f_X_L8X_2M7vF36tr4KuR4ku3bBIUdtHPncTVmx6olVrzPsbk2cr7NKJ_Pkmnsbe2dYGH9_n9_z_ZKZ7___f__7________________________3______________________________________________-4AA; _ga=GA1.2.1984547997.1682732298; pbjs-unifiedid=%7B%22TDID%22%3A%22d6409d7a-9b7b-4e73-9123-b9653bab6a12%22%2C%22TDID_LOOKUP%22%3A%22TRUE%22%2C%22TDID_CREATED_AT%22%3A%222023-03-29T01%3A38%3A18%22%7D; panoramaId_expiry=1683337098842; _cc_id=66947cf367079d3bb47e59ae405796d3; panoramaId=4fd03045f1f4e4184960a28e08d54945a702784e030d9138484cb2c9c751a62e; __gads=ID=b329119a4d1444b0:T=1682732300:S=ALNI_MbvmhuXi-G5nxhX0dyQkatK2OOqaQ; __gpi=UID=00000bff2c63abd1:T=1682732300:RT=1682732300:S=ALNI_MbZaoN1M7BQWmcFVkbOU0Nhd4KDWQ; cf_chl_2=49371a9278895cf; cf_clearance=ZOowibDnpeeIPzqC4bxcbzkn_r6jqtB6iBHtpehje4g-1682819576-0-250; _pbjs_userid_consent_data=4810923691474288; _lr_retry_request=true; _lr_geo_location=JP; cto_bundle=jcUkpF9kZFRhYXVucWRTZSUyQll4YVJlS0NTMzU1SlY2UE92SkgxQ0d3M3U4d1R0SjJhWEVSUk1BdlVjblBHNmVvQTg0ME44b1FQQ3pPVFc2VDZrZnVKT2dTRWpQcEl4cEFhVTlBa2FYa0JISHZjMCUyRkNlZiUyRjQ2SGhJeUp2N2JDVHRKWHowVTZ3dGs5N2JqbWYyMnZ4NSUyQmI4OVB1emp2TDc5MTBzMlVFa3A2VXNYSHFUOTFxUDdRZ0FqaHFnOGI3TWNKbk1uWmJmdWdtZ2NsSkRqN2cxb242WXdaeWclM0QlM0Q; cto_bidid=S7p0sV9UM25OV0FNJTJCMXB3MHJlRmhYJTJGV2ExRWQlMkJZNW5kR3AlMkY4TnhnYm9VZ2dhRXZXU3M1WVFWRnBYSjNUaDgzclhUVWM0cmRVSnlKQnk4QXpZVlVobFhaSzk2NGhTRGd5SVV5d3JhYkVEUGkweHdYbGZDRHRxM3FLTFZYd0U1NWpBYVdsa3NMeUt0a3ZFSXpPTTVralVsSUNYdyUzRCUzRA',
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
