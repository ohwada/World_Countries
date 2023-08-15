# -*- coding: utf-8 -*-
# csv2json.py
# 2023-06-01 K.OHWADA

import csv
import json


FILE_CSV= 'japan_designated_city_list.csv'

FILE_JSON= 'japan_designated_city_coordinates_list.json'


COMMA = ','

COMMA_HTML = '&comma;'

HYPHEN = '-'

EMPTY = ''

SEMICOLON = ';'

COLON_COLON = '::'


def  restore_comma(data):
    if not data:
        return EMPTY
    str_data = data.strip()
    ret = str_data.replace(COMMA_HTML, COMMA)
    return ret
#


def restore_hyphen(data):
    if not data:
        return EMPTY
    str_data = data.strip()
    if str_data == HYPHEN:
        return EMPTY
    return str_data
#


d= {}

d['name_en'] = '英語名'
d['name_city'] = '市名'
d['name_pref'] = '	都道府県'
d['url_flag'] = '市旗'
d['lat'] = '緯度'
d['lon'] = '経度'

dic = {}

dic['title'] = 'List of Japan ordinance_designated_city'

dic['title_ja'] = '政令指定都市の一覧 位置情報付き'

dic['reference'] = 'wikipedia : 政令指定都市'

dic['url_reference'] =  'https://ja.wikipedia.org/wiki/%E6%94%BF%E4%BB%A4%E6%8C%87%E5%AE%9A%E9%83%BD%E5%B8%82'

dic['item_name_ja'] = d


cities = []


with open(FILE_CSV, 'r') as f2:
    reader2 = csv.reader(f2)

    for row in reader2:
        len_row = len(row)
        print('len: ', len_row)
        if len_row < 10:
            continue
        d= {}
        d['name_city'] = row[0].strip()
        d['url_city'] = row[1].strip()
        d['name_pref'] = row[2].strip()
        d['url_pref'] = row[3].strip()
        d['url_flag'] = row[4].strip()
        d['flag_width'] = int( row[5].strip() )
        d['flag_height'] = int( row[6].strip() )
        d['name_en'] = row[7].strip()
        d['lat'] = float( row[8].strip() )
        d['lon'] = float( row[9].strip() )
        print(d)
        cities.append(d)
#

dic['cities'] = cities

with open(FILE_JSON, 'wt',  encoding='utf-8') as f2:
    json.dump(dic, f2, ensure_ascii=False)
#
