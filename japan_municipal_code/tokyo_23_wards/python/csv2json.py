# -*- coding: utf-8 -*-
# csv2json.py
# 2023-06-01 K.OHWADA

import csv
import json


FILE_CSV = 'tokyo_23_wards.csv'

FILE_JSON = 'tokyo_23_wards_list.json'


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

dic['title'] = 'List of Tokyo 23 wards'

dic['title_ja'] = '東京23区の一覧'

dic['reference'] = 'wikipedia: 東京都区部'

dic['url_reference'] =  'https://ja.wikipedia.org/wiki/%E6%9D%B1%E4%BA%AC%E9%83%BD%E5%8C%BA%E9%83%A8'

wards = []


with open(FILE_CSV, 'r') as f1:
    reader = csv.reader(f1)

    for row in reader:
        len_row = len(row)
        print('len: ', len_row)
        if len_row < 4:
            continue
        d= {}
        d['name_ward'] = row[0].strip()
        d['url_ward'] = row[1].strip()
        d['url_flag'] = row[2].strip()
        d['flag_width'] = int( row[3].strip() )
        d['flag_height'] = int( row[4].strip() )
        d['url_emblem'] = row[5].strip()
        d['emblem_width'] = int( row[6].strip() )
        d['emblem_height'] = int( row[7].strip() )
        d['population'] = restore_comma( row[8] )
        d['area'] = row[9].strip()
        d['population_density'] =restore_comma( row[10] )
        d['name_en'] = row[11].strip()
        d['lat'] = float( row[12].strip() )
        d['lon'] = float( row[13].strip() )
        print(d)
        wards.append(d)
#


dic['wards'] = wards


with open(FILE_JSON, 'wt',  encoding='utf-8') as f2:
    json.dump(dic, f2, ensure_ascii=False)
#

