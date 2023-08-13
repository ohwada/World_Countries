# json2html.py
# 2023-06-01 K.OHWADA

import json


FILE_JSON = 'data/japan_prefecture_detail_list.json'

FILE_CSV = 'japan_prefecture_list.csv'

FORMAT_LINE = '{code}, {name_pref}, {url_pref}, {name_capital}, {url_capital}, {url_flag}, {flag_width}, {flag_height} \n'


with open(FILE_JSON, 'r') as f1:
    dic = json.load(f1)
#


list_prefectures = dic['prefectures']

wdata = ''


for item in list_prefectures :
    code = item['code']
    name_pref = item['name_pref']
    url_pref = item['url_pref']
    name_capital = item['name_capital_city']
    url_capital = item['url_capital_city']
    url_flag = item['url_flag']
    flag_width = item['flag_width']
    flag_height = item['flag_height']
    line = FORMAT_LINE.format(code=code,  name_pref=name_pref, url_pref=url_pref, name_capital=name_capital, url_capital=url_capital, url_flag=url_flag, flag_width=flag_width, flag_height=flag_height)
    print(line)
    wdata +=  line
#


with open(FILE_CSV, 'wt') as f2:
    f2.write(wdata)
#

