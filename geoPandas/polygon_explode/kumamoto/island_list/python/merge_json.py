# -*- coding: utf-8 -*-
# merge_json.py
# 2023-06-01 K.OHWADA

import csv
import json
import os


FILE_CSV = 'island_list.csv'

FILE_JSON_OUT = 'kumamoto_island_list.json'

DIR = 'data'

HYPHON = '-'

ENPTY = ''


def  restore_hyphon(data):
    if not data:
        return ''
    str_data = data.strip()
    ret = str_data.replace(HYPHON, ENPTY)
    return ret
#


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



files = os.listdir(DIR)


for item in files:
    filepath =  os.path.join(DIR, item)
    with open( filepath, 'r') as f2:
        dic2 = json.load(f2)
        dic_islands = dic2['islands']
        islands += dic_islands
#


dic = {}

dic['title'] = 'List of Islands in Kumamoto'

dic['title_ja'] = '熊本県の島の一覧'

dic['reference'] = 'wikipedia: 熊本県の島'

dic['url_reference'] = 'https://ja.wikipedia.org/wiki/Category:%E7%86%8A%E6%9C%AC%E7%9C%8C%E3%81%AE%E5%B3%B6'



dic['islands'] =  islands


with open(FILE_JSON_OUT, 'wt',  encoding='utf-8') as f3:
    json.dump(dic, f3, ensure_ascii=False)
#
