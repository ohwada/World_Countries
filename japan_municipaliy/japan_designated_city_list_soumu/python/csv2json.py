# -*- coding: utf-8 -*-
# csv2json.py
# 2023-06-01 K.OHWADA

import csv
import json

FILE_CSV = 'shitei_toshi_ichiran.csv'

FILE_JSON = 'japan_designated_city_list_soumu.json'

COMMA = ','

COMMA_HTML = '&comma;'

HYPHEN = '-'

EMPTY = ''


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
d['name_ja'] = '都市'
d['population'] = '人口'
d['date'] = '移行年月日'
d['decree'] = '指定政令'


dic = {}

dic['title'] = 'List of Japan ordinance_designated_city'

dic['title_ja'] = '総務省 政令指定都市の一覧'

dic['reference'] = '総務省 : 指定都市一覧'

dic['url_reference'] =  'https://www.soumu.go.jp/main_sosiki/jichi_gyousei/bunken/shitei_toshi-ichiran.html'

dic['item_name_ja'] = d

cities = []


with open(FILE_CSV, 'r') as f1:
    reader = csv.reader(f1)

    for row in reader:
        len_row = len(row)
        print('len: ', len_row)
        if len_row < 4:
            continue
        d= {}
        d['name_ja'] = row[0].strip()
        d['population'] = restore_comma( row[1] )
        d['date'] = row[2].strip()
        d['decree'] = restore_hyphen( row[3] )
        print(d)
        cities.append(d)
#

dic['cities'] = cities

with open(FILE_JSON, 'wt',  encoding='utf-8') as f2:
    json.dump(dic, f2, ensure_ascii=False)
#
