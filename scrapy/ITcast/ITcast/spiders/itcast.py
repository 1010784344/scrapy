# -*- coding: utf-8 -*-
import scrapy
from ITcast.items import ItcastItem
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class ItcastSpider(scrapy.Spider):
    # 爬虫名，启动爬虫时需要的参数，必需
    name = 'itcast'
    # 爬取域范围，允许爬虫在这个域名下进行爬取（可选）
    allowed_domains = ['http://www.itcast.cn']
    # 起始url 列表，爬虫执行后的第一批请求，将从这个列表里来获取
    # 之后的请求从哪来？自己去解析，去提取
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']
    # 响应文件默认交给parse 方法来处理

    def parse(self, response):
        # 打印响应源码
        # print response.body
        node_list = response.xpath("//div[@class='li_txt']")
        #用来存储所有的item字段
        for node in node_list:
            #创建item字段对象，用来存储信息
            item = ItcastItem()
            # .extract()将xpath对象转换为unicode字符串（与外面稍微有点不一样）
            name = node.xpath("./h3/text()").extract()
            title = node.xpath("./h4/text()").extract()
            info = node.xpath("./p/text()").extract()

            item['name'] = name[0]
            item['title'] = title[0]
            item['info'] = info[0]
            # 返回给管道，处理一条，返回一条
            yield item

















