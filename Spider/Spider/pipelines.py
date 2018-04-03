# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import datetime


class FilePipeline(object):
    def process_item(self, item, spider):
        data = ''
        dt = datetime.datetime.now().strftime('%Y-%m-%d')
        with open('files/%s_%s.csv' % (spider.name, dt), 'a', encoding='utf-8') as f:
            row = item['row'].encode('utf-8', 'ignore').decode('utf-8', 'ignore')
            f.write(row + '\n')
            f.close()
        return item
