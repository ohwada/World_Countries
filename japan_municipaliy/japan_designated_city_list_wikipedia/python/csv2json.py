# -*- coding: utf-8 -*-
# csv2json.py
# 2023-06-01 K.OHWADA

import csv
import json

FILE_CSV = 'japan_designated_city_list_wikipedia.csv'

FILE_JSON = 'japan_designated_city_detail_list.json'

FILE_WARDS = 'wards.csv'


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
d['name_region'] = '地域'
d['name_pref'] = '	都道府県'
d['name_city'] = '市名'
d['url_emblem'] = '市章'
d['url_flag'] = '市旗'
d['estimated_population'] = '推計人口'
d['did_population'] = 'DID人口'
d['area'] = '面積'
d['urban_area'] = '市街地面積'
d['population_density'] = '人口密度'
d['did_population_density'] = 'DID人口密度'
d['financial_index'] = '財政力指数'
d['number_of_companies'] = '企業数'
d['date'] = '施行日'
d['wards'] = '行政区'


dic = {}

dic['title'] = 'List of Japan ordinance_designated_city'

dic['title_ja'] = '政令指定都市の詳細の一覧'

dic['reference'] = 'wikipedia : 政令指定都市'

dic['url_reference'] =  'https://ja.wikipedia.org/wiki/%E6%94%BF%E4%BB%A4%E6%8C%87%E5%AE%9A%E9%83%BD%E5%B8%82'

dic['item_name_ja'] = d

list_wards = []

with open(FILE_WARDS, 'r') as f1:
    reader1 = csv.reader(f1)

    for row1 in reader1:
        d= {}
        d['city'] = row1[0].strip()
        d['name_ward'] = row1[1].strip()
        d['url_ward'] = row1[2].strip()
        list_wards.append(d)
#


def collect_wards(name_city):
    wards = []
    for item in list_wards:
        city =  item['city']
        if city == name_city:
            wards.append(item)
    return wards
#


cities = []


with open(FILE_CSV, 'r') as f2:
    reader2 = csv.reader(f2)

    for row in reader2:
        len_row = len(row)
        print('len: ', len_row)
        if len_row < 21:
            continue
        d= {}
        d['name_region'] = row[0].strip()
        d['url_region'] = row[1].strip()
        d['name_pref'] = row[2].strip()
        d['url_pref'] = row[3].strip()
        name_city = row[4].strip()
        print(name_city)
        d['name_city'] = name_city
        d['url_city'] = row[5].strip()
        d['url_emblem'] = row[6].strip()
        d['emblem_width'] = int( row[7].strip() )
        d['emblem_height'] = int( row[8].strip() )
        d['url_flag'] = row[9].strip()
        d['flag_width'] = int( row[10].strip() )
        d['flag_height'] = int( row[11].strip() )
        d['estimated_population'] = restore_comma( row[12] )
        d['did_population'] = restore_comma( row[13] )
        d['area'] = restore_comma( row[14] )
        d['urban_area'] = restore_comma( row[15] )
        d['population_density'] =  row[16].strip()
        d['did_population_density'] =  row[17].strip()
        d['financial_index'] =  row[18].strip()
        d['number_of_companies'] = row[19].strip()
        d['date'] =  row[20].strip() 
        d['wards'] = collect_wards(name_city)
        print(d)
        cities.append(d)
#

dic['cities'] = cities

with open(FILE_JSON, 'wt',  encoding='utf-8') as f2:
    json.dump(dic, f2, ensure_ascii=False)
#
