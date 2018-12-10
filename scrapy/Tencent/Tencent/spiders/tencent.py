# -*- coding: utf-8 -*-
import scrapy
from Tencent.items import TencentItem

class TencentSpider(scrapy.Spider):
    # 爬虫名
    name = 'tencent'
    #爬虫爬取数据的域范围
    allowed_domains = ['hr.tencent.com']
    # 针对翻页请求
    # 之后的请求，从我们的代码里去构建
    # 1.需要拼接的url
    baseURL = 'https://hr.tencent.com/position.php?&start='
    # 1.需要拼接的url地址偏移量
    offset = 0
    # 爬虫启动时，读取的url地址列表
    start_urls = [baseURL + str(offset)]
    # 用来处理response
    def parse(self, response):
        # 提取每个response的数据
        # 节点之间求并集用‘|’
        node_list = response.xpath('//tr[@class="even"]| //tr[@class="odd"]')
        for node in node_list:
            # 构建item对象，用来保存数据
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

            # 针对数据为空的处理，如果为0，给他一个空字符串
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
            # yield 的重要性，是返回数据后还能回来接着执行代码
            yield item
        # 拼接解决翻页的问题
        # (方法一)适用场景：页面没有可以点击的请求链接，必须通过拼接url才能获取响应
        # if self.offset < 2890:
        #     self.offset += 10
        #     url = self.baseURL + str(self.offset)
        #     #有了url地址，怎么在scrapy里面创建新的请求，加关键字yield 才是发送出去
        #     # 回调函数就是请求发送出去之后，响应由哪个方法来处理
        #     yield scrapy.Request(url,callback=self.parse)
        # 拼接解决翻页的问题
        # (方法二)使用场景：直接从response获取需要爬取的链接，并发送请求处理，直到链接
        # 全部提取完
        if not response.xpath('//a[@class="noactive" and @id="next"]'):
            url = response.xpath('//a[@id="next"]/@href').extract()[0]
            yield scrapy.Request('https://hr.tencent.com/' + url, callback=self.parse)