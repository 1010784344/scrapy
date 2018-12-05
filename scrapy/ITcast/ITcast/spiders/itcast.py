# -*- coding: utf-8 -*-
import scrapy
from ITcast.items import ItcastItem
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['http://www.itcast.cn']
    # url 列表，爬虫执行后的第一批请求，将从这个列表里来获取
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']
    # 用来处理响应文件的
    def parse(self, response):
        # 打印响应源码
        # print response.body
        node_list = response.xpath("//div[@class='li_txt']")
        #用来存储所有的item字段
        for node in node_list:
            #创建item字段对象，用来存储信息
            item = ItcastItem()

            name = node.xpath("./h3/text()").extract()
            title = node.xpath("./h4/text()").extract()
            info = node.xpath("./p/text()").extract()

            item['name'] = name[0]
            item['title'] = title[0]
            item['info'] = info[0]

            yield item

















