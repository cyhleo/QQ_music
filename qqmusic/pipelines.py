# -*- coding: utf-8 -*-

import pymongo
from .items import QqmusicItem
import re
from scrapy.exceptions import DropItem


class MongoPipeline(object):
    def __init__(self, mongo_uri, mongo_db, mongo_collection):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
        self.mongo_collection = mongo_collection
    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DB'),
            mongo_collection=crawler.settings.get('MONG_COLLECTION')
        )
    def open_spider(self,spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]
        self.collection = self.db[self.mongo_collection]
    def process_item(self, item, spider):
        self.collection.insert_one(dict(item))
        return item
    def close_spider(self,spider):
        self.client.close()

class LrcPipline(object):
    """
    对item['lyric']进行清洗
    """

    def process_item(self, item, spider):
        if isinstance(item, QqmusicItem):
            if item.get('lyric'):
                lyric = item['lyric']
                pattern_1 = re.compile(r'&#\d.;', re.S)
                pattern_2 = re.compile(r'\[\d+\]', re.S)
                lyric_1 = pattern_1.sub(r'',lyric)
                lyric_2 = pattern_2.sub(r'\n', lyric_1).replace('\n\n','\n')
                item['lyric'] = lyric_2
                return item
            else:
                raise DropItem('missing item')
