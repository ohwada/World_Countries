# -*- coding: utf-8 -*-
# csv2json.py
# 2023-06-01 K.OHWADA

import csv
import json


FILE_CSV = 'place_list.csv'

FILE_JSON = 'fukushima_place_list.json'

COMMA = ','

COMMA_HTML = '&comma;'

HYPHON = '-'

ENPTY = ''


def  restore_comma(data):
    if not data:
        return ''
    str_data = data.strip()
    ret = str_data.replace(COMMA_HTML, COMMA)
    return ret
#


def  restore_hyphon(data):
    if not data:
        return ''
    str_data = data.strip()
    ret = str_data.replace(HYPHON, ENPTY)
    return ret
#


dic = {}

dic['title'] = 'List of places in Fukushima'

dic['title_ja'] = '福島県の場所の一覧'

places = []


with open(FILE_CSV, 'r') as f1:
    reader = csv.reader(f1)

    for row in reader:
        len_row = len(row)
        print('len: ', len_row)
        if len_row < 7:
            continue
        d= {}
        d['name_en'] = row[0].strip() 
        d['name_place'] = row[1].strip()
        d['url_place'] =  restore_hyphon( row[2] )
        d['name_municipality'] = row[3].strip()
        d['url_municipality'] = restore_hyphon( row[4] )
        d['lat'] = float( row[5].strip() )
        d['lon'] = float( row[6].strip() )
        print(d)
        places.append(d)
#


dic['places'] = places


with open(FILE_JSON, 'wt',  encoding='utf-8') as f2:
    json.dump(dic, f2, ensure_ascii=False)
#

