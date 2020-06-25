# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class ImgsPipeline(object):
    def __init__(self):
        self.file = open('imgs.csv','w',encoding='utf-8')

    def process_item(self, item, spider):
        data = item['title']+','+item['date']+','+item['author']+';\n'
        self.file.write(data)

    def open_spider(self,spider):
        pass

    def close_spider(self,spider):
        self.file.close()
       

