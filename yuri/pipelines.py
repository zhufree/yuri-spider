# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json
import csv
import string
class YuriPipeline:
    def open_spider(self, spider):
        if spider.name == 'nu':
            self.file = open('{}-items.csv'.format(spider.name), 'w', encoding='utf-8', newline='')
            self.writer = csv.writer(self.file)
            self.writer.writerow(['标题/Title(EN)', 'url', '已更新章节数/Chapters', '更新频率（天）/Update Frequency', 
                '读者数/Readers', '评论数/Reviews', '最后更新时间/Last Update Time',
                '作品类型/Genres', '总评分/Rating', '别名（中文名）/Title(CN)', '标签/Tags', '作者/Author', '平台/Platform', '是否翻译完成/Translaton Complete'])
        else:
            self.file = open('{}-items.json'.format(spider.name), 'w', encoding='utf-8')
        # self.url_file = open('{}-remained_url.txt'.format(spider.name), 'w', encoding='utf-8')

    def close_spider(self, spider):
        self.file.close()
        # self.url_file.close()

    def process_item(self, item, spider):
        # if type(item) == str:
        #     self.url_file.write(item + '\n')
        # else:
        if spider.name == 'nu':
            row = []
            for key, value in item.items():
                if (key == 'associated_names' or key == 'authors') and type(value) == list:
                    filtered = list(filter(lambda x: x[0] not in string.ascii_letters, value))
                    if len(filtered) > 0:
                        row.append(filtered[0].strip())
                    else:
                        row.append(value)
                else:
                    row.append(value)
            self.writer.writerow(row)
            return item
        else:
            line = json.dumps(item, ensure_ascii=False) + "\n"
            self.file.write(line)
            return item
