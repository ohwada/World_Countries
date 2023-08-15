# json2html.py
# 2023-06-01 K.OHWADA

import json

FILE_JSON = 'data/japan_designated_city_detail_list.json'

FILE_CSV= 'japan_designated_city_list.csv'


FORMAT_LINE = '{name_city}, {url_city}, {name_pref}, {url_pref}, {url_flag}, {flag_width}, {flag_height} \n'


with open(FILE_JSON, 'r') as f1:
    dic = json.load(f1)
#


list_cities= dic['cities']

wdata = ''


for item in list_cities:
    name_city = item['name_city']
    url_city = item['url_city']
    name_pref= item['name_pref']
    url_pref = item['url_pref']
    url_flag = item['url_flag']
    flag_width = item['flag_width']
    flag_height = item['flag_height']

    line = FORMAT_LINE.format( name_city=name_city, url_city=url_city,  name_pref=name_pref, url_pref=url_pref, url_flag=url_flag, flag_width=flag_width, flag_height=flag_height)
    print(line)
    wdata +=  line
#


with open(FILE_CSV, 'wt') as f2:
    f2.write(wdata)
#

