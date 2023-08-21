# -*- coding: utf-8 -*-
# csv2json.py
# 2023-06-01 K.OHWADA

import csv
import json


FILE_CSV = 'kanagawa_city_flag_list.csv'

FILE_JSON = 'kanagawa_city_flag_coordinates_list.json'


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

dic['title'] = 'List of Flag of cities in Kanagawa'

dic['title_ja'] = '神奈川県の市町村旗の一覧 位置情報付き'

dic['reference'] = 'wikipedia: 神奈川県の市町村旗一覧'

dic['url_reference'] =  'https://ja.wikipedia.org/wiki/%E7%A5%9E%E5%A5%88%E5%B7%9D%E7%9C%8C%E3%81%AE%E5%B8%82%E7%94%BA%E6%9D%91%E6%97%97%E4%B8%80%E8%A6%A7'

cities = []


with open(FILE_CSV, 'r') as f1:
    reader = csv.reader(f1)

    for row in reader:
        len_row = len(row)
        print('len: ', len_row)
        if len_row < 9:
            continue
        d= {}
        d['group'] = int( row[0].strip() )
        d['name_city'] = row[1].strip()
        d['url_city'] = row[2].strip()
        d['url_flag'] = row[3].strip()
        d['flag_width'] = int( row[4].strip() )
        d['flag_height'] = int( row[5].strip() )
        d['name_en'] = row[6].strip()
        d['lat'] = float(row[7].strip() )
        d['lon'] = float(row[8].strip() )
        print(d)
        cities.append(d)
#


dic['cities'] = cities


with open(FILE_JSON, 'wt',  encoding='utf-8') as f2:
    json.dump(dic, f2, ensure_ascii=False)
#

