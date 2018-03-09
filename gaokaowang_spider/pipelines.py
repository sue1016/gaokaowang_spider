# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import urllib
import os
class GaokaowangSpiderPipeline(object):
    def __init__(self):
        self.papers=[]
        self.file = open('gaokaowangPaperInfo.json','w')

    def process_item(self, item, spider):

        for i in range(len(item['downloadLink'])):

            paper = {}
            paper['id'] = str(i).encode('utf-8')
            paper['title'] = item['title'][i]
            paper['downloadLink'] = item['downloadLink'][i]
            self.papers.append(paper)

    def close_spider(self,spider):
        content = json.dumps(self.papers,ensure_ascii=False)
        self.file.write(content)
        self.file.close()



