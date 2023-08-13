# -*- coding: utf-8 -*-
# csv2json.py
# 2023-06-01 K.OHWADA

import csv
import json


FILE_CSV = 'tokyo_islands.csv'

FILE_JSON = 'tokyo_islands_list.json'


COMMA = ','

COMMA_HTML = '&comma;'


def  restore_comma(data):
    if not data:
        return ""
    str_data = data.strip()
    ret = str_data.replace(COMMA_HTML, COMMA)
    return ret
#


dic = {}

dic['title'] = 'List of Tokyo Islands'

dic['title_ja'] = '東京都島嶼部の自治体の一覧'

dic['reference'] = 'wikipedia: 東京都島嶼部'

dic['url_reference'] = 'https://ja.wikipedia.org/wiki/%E6%9D%B1%E4%BA%AC%E9%83%BD%E5%B3%B6%E5%B6%BC%E9%83%A8' 

municipalities = []


with open(FILE_CSV, 'r') as f1:
    reader = csv.reader(f1)

    for row in reader:
        len_row = len(row)
        print('len: ', len_row)
        if len_row < 11:
            continue
        d= {}
        d['number'] = row[0].strip()
        d['url_flag'] = row[1].strip()
        d['flag_width'] = int( row[2].strip() )
        d['flag_height'] = int( row[3].strip() )
        d['name_municipality'] = row[4].strip()
        d['url_municipality'] = row[5].strip()
        d['name_location'] = row[6].strip()
        d['url_location'] = row[7].strip()
        d['name_en'] = row[8].strip()
        d['lat'] = float( row[9].strip() )
        d['lon'] = float( row[10].strip() )
        print(d)
        municipalities.append(d)
#


dic['municipalities'] = municipalities


with open(FILE_JSON, 'wt',  encoding='utf-8') as f2:
    json.dump(dic, f2, ensure_ascii=False)
#

