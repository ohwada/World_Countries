# -*- coding: utf-8 -*-
# csv2json.py
# 2023-06-01 K.OHWADA

import csv
import json


FILE_CSV = 'tama_area.csv'

FILE_JSON = 'tokyo_tama_area_list.json'


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

dic['title'] = 'List of cities in Tokyo Tama area'

dic['title_ja'] = '東京多摩地域の市町村の一覧'

dic['reference'] = 'wikipedia: 多摩地域'

dic['url_reference'] =  'https://ja.wikipedia.org/wiki/%E5%A4%9A%E6%91%A9%E5%9C%B0%E5%9F%9F'

cities = []


with open(FILE_CSV, 'r') as f1:
    reader = csv.reader(f1)

    for row in reader:
        len_row = len(row)
        print('len: ', len_row)
        if len_row < 12:
            continue
        d= {}
        d['number'] = row[0].strip()
        d['code'] = row[1].strip()
        d['name_ja'] = row[2].strip()
        d['url_city'] = row[3].strip()
        d['url_flag'] = row[4].strip()
        d['flag_width'] = int( row[5].strip() )
        d['flag_height'] = int( row[6].strip() )
        d['population'] = restore_comma( row[7] )
        d['area'] = row[8].strip()
        d['population_density'] =restore_comma( row[9] )
        d['revenue'] = restore_comma( row[10] )
        d['established'] = row[11].strip()
        d['name_en'] = row[12].strip()
        d['lat'] = float( row[13].strip() )
        d['lon'] = float( row[14].strip() )
        print(d)
        cities.append(d)
#


dic['cities'] = cities


with open(FILE_JSON, 'wt',  encoding='utf-8') as f2:
    json.dump(dic, f2, ensure_ascii=False)
#

