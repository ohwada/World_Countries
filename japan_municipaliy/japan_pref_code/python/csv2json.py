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

dic['reference1'] = '国土交通省 : 都道府県コード'

dic['url_reference1'] =  'https://nlftp.mlit.go.jp/ksj/gml/codelist/PrefCd.html'

dic['reference2'] = '総務省 : 全国地方公共団体コード'

dic['url_reference2'] =  'https://www.soumu.go.jp/denshijiti/code.html'

prefectures = []


with open(FILE_CSV, 'r') as f1:
    reader = csv.reader(f1)

    for row in reader:
        len_row = len(row)
        print('len: ', len_row)
        if len_row < 10:
            continue
        d= {}
        d['code'] = row[0].strip()
        d['kanji'] = row[1].strip()
        d['kana'] = row[2].strip()
        d['name'] = row[3].strip() 
        d['city'] = row[4].strip() 
        d['lat'] = float( row[5].strip() )
        d['lon'] = float( row[6].strip() )
        d['url_flag'] =  row[7].strip()
        d['flag_width'] = int( row[8].strip() )
        d['flag_height'] = int( row[9].strip() )
        print(d)
        prefectures.append(d)
#

dic['prefectures'] = prefectures


with open(FILE_JSON, 'wt',  encoding='utf-8') as f2:
    json.dump(dic, f2, ensure_ascii=False)
#
