# -*- coding: utf-8 -*-
from scrapy.pipelines.images import ImagesPipeline
import scrapy
import os
from Douban.settings import IMAGES_STORE as imagebefore
# Define your item pipelines here

# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DoubanPipeline(ImagesPipeline):
    # def __init__(self):
    #     self.f = open('douban.json','w')
    def get_media_requests(self, item, info):
        image_url = item['imagelink']
        yield scrapy.Request(image_url)

    def item_completed(self, results, item, info):
        imagepath = [x['path'] for ok,x in results if ok]
        os.rename(imagebefore + imagepath[0],imagebefore + item['imagename'] + '.jpg')
