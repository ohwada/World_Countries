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

{"code": "01", "name_en": "hokkaido", "name_pref": "北海道", "url_pref": "https://ja.wikipedia.org/wiki/%E5%8C%97%E6%B5%B7%E9%81%93", "name_capital_city": "札幌市", "url_capital_city": "https://ja.wikipedia.org/wiki/%E6%9C%AD%E5%B9%8C%E5%B8%82", "url_icon": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/22/Flag_of_Hokkaido_Prefecture.svg/25px-Flag_of_Hokkaido_Prefecture.svg.png", "icon_width": 25, "icon_height": 17, "url_flag": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/22/Flag_of_Hokkaido_Prefecture.svg/800px-Flag_of_Hokkaido_Prefecture.svg.png", "flag_width": 800, "flag_height": 533, "lat": 43.064333, "lon": 141.346889}

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

dic2['title_ja'] = '都道府県の GeoJson の一覧'

dic2['reference'] = '47都道府県のポリゴンデータ'

dic2['url_reference'] = 'https://japonyol.net/editor/article/47-prefectures-geojson.html'

dic2['url_base'] = 'https://github.com/ohwada/World_Countries/blob/main/geojson/japan_prefectures_without_islands/geojson/'

dic2['url_raw_base'] = 'https://raw.githubusercontent.com/ohwada/World_Countries/main/geojson/japan_prefectures_without_islands/geojson/'

dic2['prefectures'] = prefectures


with open(FILE_OUTPUT, 'wt',  encoding='utf-8') as f2:
    json.dump(dic2, f2, ensure_ascii=False)
#



