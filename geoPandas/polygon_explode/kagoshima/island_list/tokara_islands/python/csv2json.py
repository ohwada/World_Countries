# -*- coding: utf-8 -*-
# csv2json.py
# 2023-06-01 K.OHWADA

import csv
import json


FILE_CSV = 'tokara_islands.csv'

FILE_JSON = 'tokara_islands.json'

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

dic['title'] = 'List of Islands of Tokara'

dic['title_ja'] = '吐噶喇列島の島の一覧'

dic['reference'] = 'wikipedia: 吐噶喇列島'

dic['url_reference'] = 'https://ja.wikipedia.org/wiki/Category:%E5%90%90%E5%99%B6%E5%96%87%E5%88%97%E5%B3%B6'


islands = []


with open(FILE_CSV, 'r') as f1:
    reader = csv.reader(f1)

    for row in reader:
        len_row = len(row)
        print('len: ', len_row)
        if len_row < 7:
            continue
        d= {}
        d['name_en'] = row[0].strip() 
        d['name_island'] = row[1].strip()
        d['url_island'] =  restore_hyphon( row[2] )
        d['name_municipality'] = row[3].strip()
        d['url_municipality'] = restore_hyphon( row[4] )
        d['lat'] = float( row[5].strip() )
        d['lon'] = float( row[6].strip() )
        print(d)
        islands.append(d)
#


dic['islands'] = islands


with open(FILE_JSON, 'wt',  encoding='utf-8') as f2:
    json.dump(dic, f2, ensure_ascii=False)
#
