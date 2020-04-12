# -*- coding: utf-8 -*-

BOT_NAME = 'qqmusic'

SPIDER_MODULES = ['qqmusic.spiders']
NEWSPIDER_MODULE = 'qqmusic.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# mongodb数据库信息
MONGO_URI = ''
MONGO_DB = ''
MONG_COLLECTION = ''

# 设置下载延迟
DOWNLOAD_DELAY = ''

# 请求头设置
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
   'Origin':'https://y.qq.com'
}

# 下载器中间件设置
DOWNLOADER_MIDDLEWARES = {
   'qqmusic.middlewares.RandomUserAgentDownloaderMiddleware': 543,
}

# ITEM_PIPELINES设置
ITEM_PIPELINES = {
   'qqmusic.pipelines.LrcPipline': 290,
   'qqmusic.pipelines.MongoPipeline': 300,
}


