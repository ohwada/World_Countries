# -*- coding: utf-8 -*-
# csv2json.py
# 2023-06-01 K.OHWADA

import csv
import json

FILE_CSV = 'japan_prefecture_list.csv'

FILE_JSON = 'japan_prefecture_coordinates_list.json'


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

dic['title'] = 'List of Japan prefectures coordinates'

dic['title_ja'] = '都道府県の一覧 位置情報付き'

dic['reference'] = 'wikipedia: 都道府県'

dic['url_reference'] =  'https://ja.m.wikipedia.org/wiki/%E9%83%BD%E9%81%93%E5%BA%9C%E7%9C%8C'

prefectures = []


with open(FILE_CSV, 'r') as f1:
    reader = csv.reader(f1)

    for row in reader:
        len_row = len(row)
        if len_row < 14:
            continue
        d= {}
        d['code'] = row[0].strip()
        d['name_en'] = row[1].strip()
        d['name_pref'] = row[2].strip()
        d['url_pref'] = row[3].strip()
        d['name_capital_city'] = row[4].strip()
        d['url_capital_city'] = row[5].strip()
        d['url_icon'] = row[6].strip()
        d['icon_width'] = int( row[7].strip() )
        d['icon_height'] = int( row[8].strip() )
        d['url_flag'] = row[9].strip()
        d['flag_width'] = int( row[10].strip() )
        d['flag_height'] = int( row[11].strip() )
        d['lat'] = float( row[12].strip() )
        d['lon'] = float( row[13].strip() )
        print(d)
        prefectures.append(d)
#


dic['prefectures'] = prefectures


with open(FILE_JSON, 'wt',  encoding='utf-8') as f2:
    json.dump(dic, f2, ensure_ascii=False)
#

