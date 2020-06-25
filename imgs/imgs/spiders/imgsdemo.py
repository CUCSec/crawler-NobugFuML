import scrapy
from imgs.items import *
class ImgsdemoSpider(scrapy.Spider):
    name = "imgs"
    start_urls =["https://www.woyaogexing.com/touxiang/katong/new/index.html"]

    def parse(self, response):
        title = response.css('div.pMain>div.txList>a::text').extract()
        date = response.css('div.pMain>div.txList>p>span::text').extract()
        author = response.css('div.pMain>div.txList>p>a::text').extract()
        image_urls = response.css('div.pMain>div.txList>a>img::attr("src")').extract()
        datas = zip(title,date,author,image_urls)
        for d in datas:
            img = d[3]        
            img1 = 'http:'+img  
            imgs = []           
            imgs.append(img1)   
            item = ImgsItem()
            item['title'] = '标题:' +d[0]
            item['date'] = '时间:' + d[1]
            item['author'] = '作者:' + d[2]
            item['image_urls'] = imgs
            yield item
            imgs_url = response.css('div.pageNum.wp>div.page>a::attr("href")').extract()#定位翻页
            print(len(imgs_url))
            imgs_urls = imgs_url.pop()#将15个页面全部pop出来
            next_start = response.follow(imgs_urls)
            if imgs_url is not None:#如果页面还有，就一直迭代
                yield response.follow(imgs_urls,self.parse)
