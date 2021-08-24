# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json

class YuriPipeline:
    def open_spider(self, spider):
        self.file = open('{}-items.json'.format(spider.name), 'w', encoding='utf-8')
        # self.url_file = open('{}-remained_url.txt'.format(spider.name), 'w', encoding='utf-8')

    def close_spider(self, spider):
        self.file.close()
        # self.url_file.close()

    def process_item(self, item, spider):
        # if type(item) == str:
        #     self.url_file.write(item + '\n')
        # else:
        line = json.dumps(item, ensure_ascii=False) + "\n"
        self.file.write(line)
        return item