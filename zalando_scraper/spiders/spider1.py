import scrapy
from scrapy.http import Request
from zalando_scraper.items import *


class Spider1(scrapy.Spider):
    name  = "TopsUrls"

    
    def start_requests(self):
        temp_url = 'https://www.zalando.co.uk/womens-clothing-tops/?p={}'
        link_urls = [temp_url.format(i) for i in range(2,36)]
        for url in link_urls:
            request=Request(url, callback=self.parse_product_url)
            yield (request)

		


    def parse_product_url(self,response):
        
        item  = ProductURLitem()
        producturls = response.css('a.VfpFfd').xpath('@href').getall()

        for i in range(0,len(producturls),2):
            if producturls[i][-4:] == 'html':
                item['producturl'] = producturls[i]
                yield (item)
                
    

