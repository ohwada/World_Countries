# -*- coding: utf-8 -*-
#  csv2json.py
# 2023-06-01 K.OHWADA

import csv
import json


FILE_CSV = 'designated_cities.csv'

FILE_PREF_CODE = 'data/japan_pref_code.json'

FILE_CATALOG = 'designated_cities_topojson_catalog.json'


EMPTY = ''


dic = {}

dic['title'] = 'Catalog of Japan Ordinance Designated City TopoJson'

dic['title_ja'] = '政令指定都市の TopoJson の一覧'

dic['url_base'] = 'https://geoshape.ex.nii.ac.jp/city/topojson/20230101/'

dic['reference1'] = '総務省 : 指定都市一覧'

dic['url_reference1'] = 'https://www.soumu.go.jp/main_sosiki/jichi_gyousei/bunken/shitei_toshi-ichiran.html'

dic['reference2'] = '標準地域コード 一覧 | 歴史的行政区域データセットβ版'

dic['url_reference2'] = 'https://geoshape.ex.nii.ac.jp/city/code/'


with open(FILE_PREF_CODE) as f1:
    dic1 = json.load(f1)
#

list_prefectures = dic1['prefectures']


cities = []

with open(FILE_CSV) as f2:
	reader = csv.reader(f2)
	for row in reader:
		len_row = len(row)
		if len_row < 7:
			continue
		d = {}
		d['N03_001'] = row[0].strip()
		d['N03_003'] = row[1].strip()
		d['N03_007'] = row[2].strip()
		d['id'] = row[3].strip()
		d['filepath'] = row[4].strip()
		d['name'] = row[5].strip()
		d['lat'] = float( row[6].strip() )
		d['lon'] = float( row[7].strip() )
		print(d)
		cities.append(d)
#


sort_cities = []

for item1 in list_prefectures:
	kanji = item1['kanji']
	for item2 in cities:
		n001 = item2['N03_001']
		if n001 == kanji:
			print(n001)
			sort_cities.append(item2)
#


dic['cities'] =  sort_cities

with open(FILE_CATALOG, 'wt',  encoding='utf-8') as f3:
    json.dump(dic, f3, ensure_ascii=False)
#

