# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline
from itemadapter import ItemAdapter

from datetime import datetime

class ModellbahnPipeline:

    def open_spider(self, spider):
        print("Spider geöffnet")
        
    def close_spider(self, spider):
        print("Spider geschlossen")


    def process_item(self, item, spider):
        # for key, value in ItemAdapter(item).items():
        #     print('Key: ' + key)
        #     print('Value: ' + value)
        item['ts'] = datetime.now()
        return item

class ModellbahnImagePipeline(ImagesPipeline):

    def file_path(self, request, response=None, info=None, *, item=None):
        artnr = item['artnr']
        req_filename= request.url.split('/')[-1]
        image_filename = f'{artnr}_{req_filename}.jpg'
        return image_filename

    # def get_media_requests(self, item, info):
    #     for image_url in item['image_urls']:
    #         yield scrapy.Request(image_url)

    # def item_completed(self, results, item, info):
    #     image_paths = [x['path'] for ok, x in results if ok]
    #     # if not image_paths:
    #     #     raise DropItem("Item contains no images")
    #     adapter = ItemAdapter(item)
    #     # adapter['image_paths'] = image_paths
    #     return item

