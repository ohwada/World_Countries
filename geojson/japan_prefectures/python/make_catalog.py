# make_catalog.py
# 2023-06-01 K.OHWAA


import os
import json


FILE_LIST = 'data/japan_prefecture_code_list.json'

FILE_OUTPUT = 'japan_prefecture_geojson_catalog.json'

DIR = 'geojson'


with open(FILE_LIST, 'r') as f1:
    dic1 = json.load(f1)
#


list_prefectures = dic1['prefectures']


def find_pref(pref_code, name_ja): 
	is_match = False
	matched = None
	for item in list_prefectures:
		code = item['code']
		kanji = item['kanji']
		if code == pref_code:
			is_match = True
			matched = item
			break
		if kanji == name_ja:
			is_match = True
			matched = item
			break
	return [is_match, matched]	
#


def read_geojson(filepath):
	with open(filepath) as f:
		dic = json.load(f) 
#
	features = dic['features']
	feature = features[0]
	properties = feature['properties']
	pref = properties['pref']
	name = properties['name']
	return [pref, name]
#

prefectures = []

files = os.listdir(DIR)


for  filename in files:
	path_src =  os.path.join(DIR,  filename)
	print( filename)
	code = ''
	name_en = ''
	lat = 0
	lon = 0
	pref_code, name_ja = read_geojson(path_src)
	is_match, matched = item =find_pref(pref_code, name_ja)
	if is_match:
		code = matched['code']
		name_en = matched['name']
		lat = matched['lat']
		lon = matched['lon']
	d = {}
	d['code'] = code
	d['name_en'] = name_en
	d['name_ja'] = name_ja
	d['lat'] = lat
	d['lon'] = lon
	d['filename'] = filename
	prefectures.append(d)
#

sort_prefectures = []

for item2 in list_prefectures:
		code2 = item2['code']
		kanji = item2['kanji']
		for item3 in prefectures:
			code3 = item3['code']
			name_ja = item3['name_ja']
			if (code2 == code3) or (kanji == name_ja):
				sort_prefectures.append(item3)
#				


dic2 = {}

dic2['title'] = 'List of Japan Prefectures GeoJson'

dic2['title_ja'] = '都道府県の GeoJson の一覧'

dic2['reference'] = '47都道府県のポリゴンデータ'

dic2['url_reference'] = 'https://japonyol.net/editor/article/47-prefectures-geojson.html'

dic2['url_base'] = 'https://github.com/ohwada/World_Countries/blob/main/geojson/japan_prefectures/geojson/'

dic2['url_raw_base'] = 'https://raw.githubusercontent.com/ohwada/World_Countries/main/geojson/japan_prefectures/geojson/'

dic2['prefectures'] = sort_prefectures


with open(FILE_OUTPUT, 'wt',  encoding='utf-8') as f2:
    json.dump(dic2, f2, ensure_ascii=False)
#



