# QQ_music
为获得qq音乐网站流行音乐排行榜中各音乐的数据，对域名为'qq.com'的QQ音乐网站进行自动爬取，本项目仅模拟12月3号这一天流行音乐排行榜信息的抓取，更改spider文件TopMusicSpider类中的data参数，可以获得其他日期的流行音乐排行榜数据。    
每条数据包含如下字段：排名、歌曲名、唱片、歌手、时长、歌词。

# 部分结果展示



# 项目说明

1. 使用scrapy框架来编写爬虫程序，编写QqmusicItem类，该类继承于scrapy.Item，为item添加排名、歌曲名、唱片、歌手等字段。
2. 编写下载器中间件RandomUserAgentDownloaderMiddleware，该类使用使用fake_useragent库，实现随机获取User-Agent，并赋值给请求头。
3. 在settings中构造包含Host、Accept-Encoding等信息的请求头，模拟浏览器行为。
4. 在setting中设置下载延迟DOWNLOAD_DELAY，防止因为访问频繁，被目标服务器禁止ip访问。
5. 编写LrcPipline类,对lyric字段数据进行清洗。
6. 编写LianjiaHomePipeline类，将下载的数据保存至MongoDB数据库。


# 运行方法

执行run.py


# 告示

本代码仅作学习交流，切勿用于商业用途。如涉及侵权，请邮箱联系，会尽快删除。

