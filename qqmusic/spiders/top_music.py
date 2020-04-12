# -*- coding: utf-8 -*-
import scrapy
from ..items import QqmusicItem
import json

class TopMusicSpider(scrapy.Spider):
    name = 'top_music'
    allowed_domains = ['qq.com']
    data = "2019-12-03"
    rank_url = 'https://u.y.qq.com/cgi-bin/musicu.fcg?-=getUCGI7439951166930805&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf8&notice=0&platform=yqq.json&needNewCode=0&data={"detail":{"module":"musicToplist.ToplistInfoServer","method":"GetDetail","param":{"topId":4,"offset":0,"num":100,"period":{}}},"comm":{"ct":24,"cv":0}}'.format(data)
    start_urls = [rank_url]

    def parse(self, response):

        dict_music = json.loads(response.text)
        songInfoList = dict_music['detail']['data'].get('songInfoList')
        song_rank_info = dict_music['detail']['data']['data'].get('song')
        rank_dict={}
        for rank_info in song_rank_info:
            rank_id = rank_info['songId']
            rank_num = rank_info['rank']
            rank_dict[rank_id] = rank_num
        self.logger.debug('rank_dict:{}'.format(rank_dict))

        for song in songInfoList:
            song_name = song.get('name')
            album = song['album'].get('name')
            singer = song['singer'][0].get('name')
            interval = song['interval']
            id = song['id']
            rank = rank_dict[id]
            url = 'https://c.y.qq.com/lyric/fcgi-bin/fcg_query_lyric_yqq.fcg?nobase64=1&musicid={}&-=jsonp1&g_tk=5381&format=json&inCharset=utf8&outCharset=utf-8&platform=yqq.json'.format(id)
            yield scrapy.Request(url,meta={'song_name':song_name,'album':album,'singer':singer,'interval':interval,'id':id, 'rank':rank}, callback=self.parse_lyric, dont_filter=True)

    def parse_lyric(self, response):
        print(response.text)
        item = QqmusicItem()
        song_name = response.meta.get('song_name')
        album = response.meta.get('album')
        singer = response.meta.get('singer')
        interval = response.meta.get('interval')
        rank = response.meta.get('rank')
        item['rank'] = rank
        item['song_name'] = song_name
        item['album'] = album
        item['singer'] = singer
        item['interval'] = interval
        lyr_dict = json.loads(response.text)
        item['lyric'] = lyr_dict['lyric']
        yield item
