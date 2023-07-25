# -*- coding: utf-8 -*-
# csv2json.py
# 2023-06-01 K.OHWADA

import csv
import json


dic = {}

dic['title'] = 'Japan Prefectures code'

dic['title_ja'] = '都道府県コード'

dic['reference1'] = '国土交通省 : 都道府県コード'

dic['url_reference1'] =  'https://nlftp.mlit.go.jp/ksj/gml/codelist/PrefCd.html'

dic['reference2'] = '総務省 : 全国地方公共団体コード'

dic['url_reference2'] =  'https://www.soumu.go.jp/denshijiti/code.html'

prefectures = []


with open('japan_pref_code.csv') as f1:
    reader = csv.reader(f1)

    for row in reader:
        len_row = len(row)
        print('len: ', len_row)
        if len_row < 4:
            continue
        d= {}
        d['code'] = row[0].strip()
        d['kanji'] = row[1].strip()
        d['kana'] = row[2].strip()
        d['name'] = row[3].strip() 
        print(d)
        prefectures.append(d)
#

dic['prefectures'] = prefectures

with open('japan_pref_code.json', 'wt') as f2:
    json.dump(dic, f2)
#
