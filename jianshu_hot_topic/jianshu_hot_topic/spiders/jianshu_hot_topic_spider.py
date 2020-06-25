import random
from time import sleep
from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector
from scrapy.http import Request
from jianshu_hot_topic.items import JianshuHotTopicItem
 
class jianshu_hot_topic(CrawlSpider):


    name = "jianshu_hot_topic"
    start_urls = ["https://www.jianshu.com/recommendations/collections?page=2&order_by=hot"]
 
    def parse(self,response):


        item = JianshuHotTopicItem()
        selector = Selector(response)
        collections = selector.xpath('//div[@class="col-xs-8"]')   
        for collection in collections:
            collection_name = collection.xpath('div/a/h4/text()').extract()[0].strip()
            collection_description = collection.xpath('div/a/p/text()').extract()[0].strip()
            collection_article_count = collection.xpath('div/div/a/text()').extract()[0].strip().replace('篇文章','')
            collection_attention_count = collection.xpath('div/div/text()').extract()[0].strip().replace("人关注",'').replace("· ",'')
            
            item['collection_name'] = collection_name
            item['collection_description'] = collection_description
            item['collection_article_count'] = collection_article_count
            item['collection_attention_count'] = collection_attention_count
 
            yield item
         
         
        urls = ['https://www.jianshu.com/recommendations/collections?page={}&order_by=hot'.format(str(i)) for i in range(3,11)]
        for url in urls:
            sleep(random.randint(2,7))
            yield Request(url,callback=self.parse)