# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


import csv
 
class JianshuHotTopicPipeline(object):
    
    def process_item(self, item, spider):

        f =  open('zhuanti.csv','a+',encoding='utf-8')
        writer = csv.writer(f)
        writer.writerow((item['collection_name'],item['collection_description'],item['collection_article_count'],item['collection_attention_count']))
        
        return item