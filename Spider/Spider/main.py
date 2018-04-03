from scrapy import cmdline
import os
from Spider.common_util.common_util.datetime_util import add_date
import time


def re_write_file(file_path):
    f = open(file_path, 'w')
    f.write(','.join(['date', 'app_name', 'apk_name', 'big_class', 'label', 'market']) + '\n')
    f.close()

dt = add_date(0).strftime('%Y-%m-%d')
re_write_file(r'D:\pyproject\spider\Spider\Spider\files\wdj_spider_%s.csv' % dt)
re_write_file(r'D:\pyproject\spider\Spider\Spider\files\xm_spider_%s.csv' % dt)
re_write_file(r'D:\pyproject\spider\Spider\Spider\files\tx_spider_%s.csv' % dt)
re_write_file(r'D:\pyproject\spider\Spider\Spider\files\bd_spider_%s.csv' % dt)
re_write_file(r'D:\pyproject\spider\Spider\Spider\files\x360_spider_%s.csv' % dt)
re_write_file(r'D:\pyproject\spider\Spider\Spider\files\mmy_spider_%s.csv' % dt)

os.system("scrapy crawl wdj_spider")
time.sleep(2)
os.system("scrapy crawl xm_spider")
time.sleep(2)
os.system("scrapy crawl tx_spider")
time.sleep(2)
os.system("scrapy crawl bd_spider")
time.sleep(2)
os.system("scrapy crawl x360_spider")
time.sleep(2)
os.system("scrapy crawl mmy_spider")
time.sleep(2)
# �ϲ���ȡ����ļ�
os.system("python ../scripts/spider_file_scripts/merge_files.py")
