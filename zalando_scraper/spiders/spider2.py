import scrapy
import csv
from scrapy.http import Request
from zalando_scraper.items import *


class Spider2(scrapy.Spider):
    
    name  = "Tops"
    counter = 0
    priority = 0
    
    def start_requests(self):
        
        base_url = 'https://www.zalando.co.uk'
        
        with open("D:/zalando_scraper/urls.csv", "r") as f:
            reader=csv.DictReader(f)
    
            for row in reader:
                url = base_url+row['producturl']
                self.priority+=1
                yield Request(url,callback = self.parse_product_page,priority=self.priority)
                 
        
    def parse_product_page(self,response):
        
        item  = TopDetails()
        self.counter+=1
        item['id_'] = self.counter
        item['brand'] = response.css('h3.OEhtt9::text').get()
        item['productName'] = response.css('h1.OEhtt9::text').get()
        item['price'] = response.css('span.uqkIZw::text').get()

        image_urls_w156 = response.css('img._6uf91T').xpath('@src').getall()[0:5]
        image_urls = []
        for image in image_urls_w156:
            image_urls.append(image.split('?')[0])

        return item,ImgData(id_= str(self.counter),image_urls = image_urls)


