import scrapy
from project1.items import Project1Item
class ScrapySpider(scrapy.Spider):
    name="data"
    start_urls=[
    'http://dmoztools.net/Arts/Architecture/',
    'http://dmoztools.net/Business/E-Commerce/Developers/'
    ]

    def parse(self,response):
        sites =response.xpath('//*[@id="site-list-content"]/div')
        a=[]
        for site in sites:
            b=Project1Item()
            b['name']=site.xpath('div/a/div/text()').extract()[0]
            b['url']=site.xpath('div/a/@href').extract()[1]
        
            a.append(b)
        return a