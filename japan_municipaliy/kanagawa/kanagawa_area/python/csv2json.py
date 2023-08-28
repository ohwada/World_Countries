# -*- coding: utf-8 -*-
# csv2json.py
# 2023-06-01 K.OHWADA

import csv
import json


FILE_CSV = 'csv/kanagawa_area.csv'


FILE_JSON = 'kanagawa_area_list.json'

FORMAT_FILE = 'csv/{name}.csv'


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

dic['title'] = 'List of Kanagawa areas'

dic['title_ja'] = '神奈川県の地域と市町村の一覧'

dic['reference1'] = '神奈川県: 神奈川県内の市町村'

dic['url_reference1'] =  'https://www.pref.kanagawa.jp/docs/ie2/cnt/f530001/p780102.html'

dic['reference2'] = 'wikipedia: 神奈川県'

dic['url_reference2'] = 'https://ja.wikipedia.org/wiki/%E7%A5%9E%E5%A5%88%E5%B7%9D%E7%9C%8C'


def read_csv(filepath):
    cities = []
    with open(filepath, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            len_row = len(row)
            print('len: ', len_row)
            if len_row < 4:
                continue
            d= {}
            d['group'] = int( row[0].strip() )
            d['name_en'] = row[1].strip()
            d['name_city'] = row[2].strip()
            d['url_city'] = row[3].strip()
            print(d)
            cities.append(d)
    return cities
#


areas = []


with open(FILE_CSV, 'r') as f1:
    reader = csv.reader(f1)

    for row in reader:
        len_row = len(row)
        print('len: ', len_row)
        if len_row < 3:
            continue
        d= {}
        name_en = row[0].strip()
        d['name_en'] = name_en
        d['name_area'] = row[1].strip()
        d['url_area'] = row[2].strip()
        filepath = FORMAT_FILE.format(name=name_en)
        d['cities'] = read_csv(filepath)
        print(d)
        areas.append(d)
#


dic['areas'] = areas


with open(FILE_JSON, 'wt',  encoding='utf-8') as f2:
    json.dump(dic, f2, ensure_ascii=False)
#

