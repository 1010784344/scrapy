# -*- coding: utf-8 -*-
from scrapy.pipelines.images import ImagesPipeline
import scrapy
import os
# settings 里面的配置可以在代码里读取的
from settings import IMAGES_STORE as images_store
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

class DouyuPipeline(ImagesPipeline):
    # 本身为系统自带方法重写，专门返回一个请求的
    # 相当于获取在爬虫文件的图片链接，传给了管道，管道就会拿到我们图片链接，去发送请求
    # 获取媒体文件的一个请求
    def get_media_requests(self, item, info):
        image_link = item['imagelink']
        yield scrapy.Request(image_link)

    # 自带方法重写，我们用这个方法主要使用results 这个参数，会获取图片的文件名
    # results 数据格式如下：[(True, {'url': 'https://rpic.douyucdn.cn/asrpic/181211/5838659_1950.jpg/dy1', '
    # path': 'full/ffbbc4d4e9f127b4c6f35f1b394376be3ea4fbac.jpg', 'checksum': '80914ae
    # ac65e842151a38a9df3fd1628'})]
    def item_completed(self, results, item, info):
        # 取出results里图片信息中的图片路径的值
        image_path = [x['path']for ok,x in results if ok]

        #修改文件名
        os.rename(images_store + image_path[0], images_store +item['nickname'] + '.jpg')
        return item
