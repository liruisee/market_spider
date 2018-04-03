from Spider.common_util.common_util import un_tem_file_path
from Spider.common_util.common_util.datetime_util import add_date

dt = add_date(0).strftime('%Y-%m-%d')
file_path = un_tem_file_path + '/spider_files/spider_%s.csv' % dt

f = open(file_path, 'r', encoding='utf-8')
for line in f.readlines():
    if ';' in line:
        print(line)
f.close()
