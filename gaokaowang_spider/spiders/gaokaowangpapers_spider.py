# -*- coding: utf-8 -*-
import scrapy
from gaokaowang_spider.items import GaokaowangSpiderItem
from scrapy.selector import Selector
from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.linkextractor import LinkExtractor
from scrapy.http import Request
'''
cd /Users/yuandarong/gaokaowang_spider/gaokaowang_spider
scrapy crawl gaokaowangpapers_spider
'''

class GaokaowangSpider(CrawlSpider):

    name = 'gaokaowang_spider'
    start_urls = ['http://tiku.gaokao.com/gaokao//ht?pg=10']
    rules = (
        Rule(LinkExtractor(allow=(r'\?pg=\d+')),callback = 'parse_item',follow = True),)

    def parse_item(self, response):
        print response

        sel = Selector(response)
        item = GaokaowangSpiderItem()

        title = sel.xpath('//article[@class="result-item"]/h2/a/text()').extract()
        downloadLink = sel.xpath('//article[@class="result-item"]//a[@class = "download"]/@href').extract()

        item['title'] = [n.encode('utf-8')for n in title]
        item['downloadLink'] = [n.encode('utf-8') for n in downloadLink]

        yield item