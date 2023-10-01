# make_catalog.py
# 2023-06-01 K.OHWAA


import os
import json


FILE_LIST = 'data/japan_prefecture_coordinates_list.json'

FILE_OUTPUT = 'japan_prefecture_without_islands_geojson_catalog.json'

FORMAT_FILENAME = '{name}.geojson'

DIR = 'geojson'


with open(FILE_LIST, 'r') as f1:
    dic1 = json.load(f1)
#


list_prefectures = dic1['prefectures']

prefectures = []

for item in list_prefectures:
	code = item['code']
	name_en = item['name_en']
	name_pref = item['name_pref']
	lat = item['lat']
	lon = item['lon']
	print(name_pref)
	filename = FORMAT_FILENAME.format(name=name_en)
	filepath =  os.path.join(DIR,  filename)
	is_file = os.path.isfile(filepath)
	if is_file:
		d = {}
		d['code'] = code
		d['name_en'] = name_en
		d['name_ja'] = name_pref
		d['lat'] = lat
		d['lon'] = lon
		d['filename'] = 	filename
		prefectures.append(d)
	else:
		print('not exist')
		exit()
#


dic2 = {}

dic2['title'] = 'List of Japan Prefectures GeoJson'

dic2['title_ja'] = '島部のポリゴンを除いて 内陸部のポリゴンにした都道府県の GeoJson の一覧'

dic2['reference'] = '47都道府県のポリゴンデータ'

dic2['url_reference'] = 'https://japonyol.net/editor/article/47-prefectures-geojson.html'

dic2['url_base'] = 'https://github.com/ohwada/World_Countries/blob/main/geojson/japan_prefectures_without_islands/geojson/'

dic2['url_raw_base'] = 'https://raw.githubusercontent.com/ohwada/World_Countries/main/geojson/japan_prefectures_without_islands/geojson/'

dic2['prefectures'] = prefectures


with open(FILE_OUTPUT, 'wt',  encoding='utf-8') as f2:
    json.dump(dic2, f2, ensure_ascii=False)
#



