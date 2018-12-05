# -*- coding: utf-8 -*-
import json
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ItcastPipeline(object):
    def __init__(self):
        self.f = open("itcast_pipline.json","w")

    def process_item(self, item, spider):
        # item 是从 itcast 处理完传过来的。item类似字典但也还是需要强转。有中文的情况ensure，中文会
        # 按unincode 存储
        connect = json.dumps(dict(item),ensure_ascii = False) + ',\n'
        self.f.write(connect.encode('utf-8'))
        # 返回给引擎
        return item

    def close_spider(self,spider):
        self.f.close()
