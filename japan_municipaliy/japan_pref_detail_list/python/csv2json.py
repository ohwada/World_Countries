# -*- coding: utf-8 -*-
# csv2json.py
# 2023-06-01 K.OHWADA

import csv
import json

FILE_CSV = 'japan_pref_list.csv'

FILE_JSON = 'japan_prefecture_detail_list.json'


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

dic['title'] = 'List of Japan prefectures detail'

dic['title_ja'] = '都道府県の詳細の一覧'

dic['reference'] = 'wikipedia: 都道府県'

dic['url_reference'] =  'https://ja.m.wikipedia.org/wiki/%E9%83%BD%E9%81%93%E5%BA%9C%E7%9C%8C'

prefectures = []

FORMAT_LINE = '{code}, {name_pref}, {url_pref}, {yomi}, {name_capital},  {url_capital}, {name_largest_city}, {url_largest_city}, {url_flag}, {flag_width}, {flag_height}, {name_region}, {url_region}, {population}, {area}, {density}, {number_of_cities}, {diet_constant} \n'



with open(FILE_CSV, 'r') as f1:
    reader = csv.reader(f1)

    for row in reader:
        len_row = len(row)
        print('len: ', len_row)
        if len_row < 17:
            continue
        d= {}
        d['code'] = row[0].strip()
        d['name_pref'] = row[1].strip()
        d['url_pref'] = row[2].strip()
        d['yomi'] = row[3].strip()
        d['name_capital_city'] = row[4].strip()
        d['url_capital_city'] = row[5].strip()
        d['name_largest_city'] = row[6].strip()
        d['url_largest_city'] = row[7].strip()
        d['url_flag'] = row[8].strip()
        d['flag_width'] = int( row[9].strip() )
        d['flag_height'] = int( row[10].strip() )
        d['region'] = row[11].strip()
        d['population'] = restore_comma( row[12] )
        d['area'] = restore_comma( row[13].strip() )
        d['population_density'] = restore_comma( row[14] )
        d['number_of_cities'] = int( row[15].strip() )
        d['diet_member_quota'] = row[16].strip()
        print(d)
        prefectures.append(d)
#


dic['prefectures'] = prefectures


with open(FILE_JSON, 'wt',  encoding='utf-8') as f2:
    json.dump(dic, f2, ensure_ascii=False)
#

