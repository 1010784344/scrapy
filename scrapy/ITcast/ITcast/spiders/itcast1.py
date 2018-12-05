# -*- coding: utf-8 -*-
import scrapy


class Itcast1Spider(scrapy.Spider):
    name = 'itcast1'
    allowed_domains = ['http://www.baidu.com']
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        pass
