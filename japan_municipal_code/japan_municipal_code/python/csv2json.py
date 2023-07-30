# -*- coding: utf-8 -*-
# csv2json.py
# 2023-06-01 K.OHWADA

import csv
import json


FILE_CSV = 'japan_municipal_code.csv'

FILE_JSON = 'japan_municipal_code.json'

d= {}
d['code'] = '団体コード'
d['pref_kanji'] = '都道府県名 (漢字)'
d['city_kanji'] = '市区町村名 (漢字)'
d['pref_kana'] = '都道府県名 (カナ)'
d['city_kana'] =  '市区町村名 (カナ)'

dic = {}

dic['title'] = 'Japan  Municipal Code'

dic['title_ja'] = '全国地方公共団体コード'

dic['reference'] = '総務省 : 全国地方公共団体コード'

dic['url_reference'] =  'https://www.soumu.go.jp/denshijiti/code.html'

dic['item_name_ja'] = d

cities = []


with open(FILE_CSV, 'r') as f1:
    reader = csv.reader(f1)

    for row in reader:
        len_row = len(row)
        print('len: ', len_row)
        if len_row < 5:
            continue
        d= {}
        d['code'] = row[0].strip()
        d['pref_kanji'] = row[1].strip()
        d['city_kanji'] = row[2].strip()
        d['pref_kana'] = row[3].strip()
        d['city_kana'] = row[4].strip() 
        print(d)
        cities.append(d)
#

dic['cities'] = cities

with open(FILE_JSON, 'wt',  encoding='utf-8') as f2:
    json.dump(dic, f2, ensure_ascii=False)

