# -*- coding: utf-8 -*-
from Spider.common_util.common_util.datetime_util import add_date
from os.path import dirname,abspath
import sys
import io
# 设置标准输出解决乱码问题
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')

# 今天日期
dt = add_date(0).strftime('%Y-%m-%d')
# 今天产生的爬虫文件
file_list = [r'D:\pyproject\spider\Spider\Spider\files\wdj_spider_%s.csv' % dt,
             r'D:\pyproject\spider\Spider\Spider\files\xm_spider_%s.csv' % dt,
             r'D:\pyproject\spider\Spider\Spider\files\tx_spider_%s.csv' % dt,
             r'D:\pyproject\spider\Spider\Spider\files\bd_spider_%s.csv' % dt,
             r'D:\pyproject\spider\Spider\Spider\files\x360_spider_%s.csv' % dt,
             r'D:\pyproject\spider\Spider\Spider\files\mmy_spider_%s.csv' % dt,
             ]

for tem in file_list:
    print(tem)

# 当前文件路径
file_path = dirname(dirname(dirname(abspath(__file__)))) + '/file_log/un_tem_file/spider_files/spider_%s.csv' % dt

# 将原始爬取的文件在内存中合并，存入dic_data中
dic_data = {}
for file in file_list:
    f = open(file, 'r', encoding='utf-8')
    f.readline()
    while 1:
        line = f.readline()
        if line:
            line = line.replace('\r', '').replace('\n', '')
            dt, app_name, apk_name, big_class, label, market = line.split(',')
            if apk_name not in dic_data:
                dic_data[apk_name] = [dt, {app_name}, apk_name, {big_class}, {label}, {market}]
            else:
                dic_data[apk_name][1].add(app_name)
                dic_data[apk_name][3].add(big_class)
                dic_data[apk_name][4].add(label)
                dic_data[apk_name][5].add(market)
        else:
            break
    f.close()

# 将所有集合转字符串，分号间隔
for apk_name in dic_data:
    dic_data[apk_name][1] = ';'.join(sorted(list(filter(lambda x: x != '', dic_data[apk_name][1]))))
    dic_data[apk_name][3] = ';'.join(sorted(list(filter(lambda x: x != '', dic_data[apk_name][3]))))
    dic_data[apk_name][4] = ';'.join(sorted(list(filter(lambda x: x != '', dic_data[apk_name][4]))))
    dic_data[apk_name][5] = ';'.join(sorted(list(filter(lambda x: x != '', dic_data[apk_name][5]))))

# 将数据结果按照应用市场名称排序
result_list = sorted(list(dic_data.values()), key=lambda x: x[5], reverse=False)
dic_data.clear()

# 要合并写入的文件
f_all = open(file_path, 'w', encoding='utf-8')
f_all.write(','.join(['date', 'app_name', 'apk_name', 'big_class', 'label', 'market']) + '\n')
for row in result_list:
    if row[4].count(',') > 0:
        print(row)
    f_all.write(','.join(row) + '\n')
f_all.close()
