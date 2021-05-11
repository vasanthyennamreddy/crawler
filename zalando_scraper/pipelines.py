# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import os, os.path, shutil
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import *
from scrapy.utils.project import get_project_settings



class ZalandoScraperPipeline:
    def process_item(self, item, spider):
        return item

class CustomImagesPipeline(ImagesPipeline):
    def item_completed(self, results, item, info):
        
        settings = get_project_settings()
        storage = settings.get('IMAGES_STORE')
        
        if len(results) > 0:

            for res in results:
                ok,result = res

                path_ = result['path']
                target_path = os.path.join(storage,item['id_'])
                path_ = os.path.join(storage,path_)

                if not os.path.exists(os.path.join(storage, item['id_'])):
                    os.makedirs(os.path.join(storage, item['id_']))

                shutil.move(path_, target_path)

            """for res in results:
                x,result = res
                if self.IMAGES_RESULT_FIELD in item.fields:
                    result['path'] = target_path
                    item[self.IMAGES_RESULT_FIELD].append(result)"""

        return item
        
       
        
        
        
        


        