# -*- coding: utf-8 -*-
import scrapy
import json
from Douyu.items import DouyuItem
class DouyuSpider(scrapy.Spider):
    name = 'douyu'
    allowed_domains = ['douyucdn.cn']
    baseurl = 'http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset='
    offset = 0
    start_urls = [baseurl+str(offset)]

    def parse(self, response):
        # 针对响应json的处理办法
        data_list = json.loads(response.body)['data']
        if len(data_list) == 0:
            return
        for data in data_list:
            # 可以不通过管道，将1数据打印出来
            # print data['nickname']
            # print data['vertical_src']
            # print '*'*40
            item = DouyuItem()
            item['nickname'] = data['nickname']
            item['imagelink'] = data['vertical_src']

            yield item
        self.offset += 20
        yield scrapy.Request(self.baseurl + str(self.offset), callback=self.parse)















