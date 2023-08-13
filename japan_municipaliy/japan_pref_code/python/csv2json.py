# -*- coding: utf-8 -*-
# csv2json.py
# 2023-06-01 K.OHWADA

import csv
import json

FILE_CSV  = 'japan_pref_code.csv'

FILE_JSON = 'japan_prefecture_code_list.json'


dic = {}

dic['title'] = 'List of Japan Prefecture code'

dic['title_ja'] = '都道府県コードの一覧'

dic['reference'] = '国土交通省 : 都道府県コード'

dic['url_reference'] =  'https://nlftp.mlit.go.jp/ksj/gml/codelist/PrefCd.html'

prefectures = []


with open(FILE_CSV, 'r') as f1:
    reader = csv.reader(f1)

    for row in reader:
        len_row = len(row)
        print('len: ', len_row)
        if len_row < 3:
            continue
        d= {}
        d['code'] = row[0].strip()
        d['name_en'] = row[1].strip()
        d['name_ja'] = row[2].strip()
        print(d)
        prefectures.append(d)
#

dic['prefectures'] = prefectures


with open(FILE_JSON, 'wt',  encoding='utf-8') as f2:
    json.dump(dic, f2, ensure_ascii=False)
#
