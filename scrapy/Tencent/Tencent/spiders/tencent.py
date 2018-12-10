# -*- coding: utf-8 -*-
import scrapy
from Tencent.items import TencentItem

class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['hr.tencent.com']
    # 针对翻页请求
    # 之后的请求，从我们的代码里去构建
    baseURL = 'https://hr.tencent.com/position.php?&start='
    offset = 0
    start_urls = [baseURL + str(offset)]

    def parse(self, response):
        # 节点之间求并集用‘|’
        node_list = response.xpath('//tr[@class="even"]| //tr[@class="odd"]')
        for node in node_list:
            item = TencentItem()
            # 以下node.path 表达式都 得加一个点
            # extract是把xpath对象转换为unicode字符串
            #
            positionName = node.xpath('./td[1]/a/text()').extract()
            # 获取属性值的时候，不需要提取文本，所以不用text（）
            positionLink = node.xpath('.//a/@href').extract()
            positionType = node.xpath('./td[2]/text()').extract()
            peopleNumber = node.xpath('./td[3]/text()').extract()
            workLocation = node.xpath('./td[4]/text()').extract()
            publishTime = node.xpath('./td[5]/text()').extract()

            #把unicode 对象转换为 utf-8 格式

            # 针对数据为空的处理
            if positionName:
                item['positionName'] = positionName[0].encode('utf-8')
            else:
                item['positionName'] = ''
            if positionLink:
                item['positionLink'] = positionLink[0].encode('utf-8')
            else:
                item['positionLink'] = ''
            if positionType:
                item['positionType'] = positionType[0].encode('utf-8')
            else:
                item['positionType'] = ''
            if peopleNumber:
                item['peopleNumber'] = peopleNumber[0].encode('utf-8')
            else:
                item['peopleNumber'] = ''

            if workLocation:
                item['workLocation'] = workLocation[0].encode('utf-8')
            else:
                item['workLocation'] = ''
            if publishTime:
                item['publishTime'] = publishTime[0].encode('utf-8')
            else:
                item['publishTime'] = ''

            yield item
        # 拼接解决翻页的问题
        if self.offset < 2890:
            self.offset += 10
            url = self.baseURL + str(self.offset)
            #有了url地址，怎么在scrapy里面创建新的请求，加关键字yield 才是发送出去
            # 回调函数就是请求发送出去之后，响应由哪个方法来处理
            yield scrapy.Request(url,callback=self.parse)

