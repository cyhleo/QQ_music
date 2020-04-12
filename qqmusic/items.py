# -*- coding: utf-8 -*-


import scrapy

class QqmusicItem(scrapy.Item):
    # define the fields for your item here like:
    #排名
    rank = scrapy.Field()
    #歌曲名
    song_name = scrapy.Field()
    #唱片
    album = scrapy.Field()
    #歌手
    singer = scrapy.Field()
    #时长
    interval = scrapy.Field()
    #歌词
    lyric = scrapy.Field()
