# -*- coding: utf-8 -*-
import scrapy
from Douban.items import DoubanItem

class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['movie.douban.com']
    baseurl = 'https://movie.douban.com/top250'
    url =baseurl + '?start=0'
    start_urls = [url]

    def parse(self, response):
        node_list = response.xpath("//div[@class='pic']//img")
        for node in node_list:
            item = DoubanItem()
            item['imagename'] = node.xpath("./@alt")[0].extract()
            item['imagelink'] = node.xpath("./@src")[0].extract()

            yield item

        # if self.offset < 225:
        #     self.offset += 25
        #     newurl = self.baseurl + str(self.offset)
        #     yield scrapy.Request(newurl, callback = self.parse)

        if response.xpath("//span[@class = 'next']/link/@href"):
            offset = response.xpath("//span[@class = 'next']/link/@href").extract()[0]
            newurl = self.baseurl + offset
            yield scrapy.Request(newurl, callback=self.parse)












