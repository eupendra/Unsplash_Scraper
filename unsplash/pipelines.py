# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter


# class UnsplashPipeline:
#     def process_item(self, item, spider):
#         return item
from scrapy.pipelines.images import ImagesPipeline

class UnsplashImagesPipeline(ImagesPipeline):
        def file_path(self, request, response=None, info=None, *, item=None):
            kind=item.get('kind','unknown')
            search=item.get('search','unknown')
            prefix = '_'.join(item.get('tags'))
            image_name = prefix +'_'+item.get('id')
            return f'{search}/{kind}/{image_name}.jpg'
