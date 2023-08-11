# rename.py
# 2023-06-01 K.OHWAA

import os
import json
import shutil


FILE_LIST = 'data/japan_prefecture_code_list.json'


DIR_SRC = 'splited'

DIR_DST = 'geojson'

FORMAT_FILE_NAME = '{name}.geojson'


if not os.path.isdir(DIR_DST):
    os.mkdir(DIR_DST)
#


with open(FILE_LIST, 'r') as f1:
    dic = json.load(f1)
#


list_prefectures = dic['prefectures']


def find_pref(pref_code, name_ja): 
	is_match = False
	name = None
	for item in list_prefectures:
		code = item['code']
		kanji = item['kanji']
		name = item['name']
		if code == pref_code:
			is_match = True
			break
		if kanji == name_ja:
			is_match = True
			break
	return [is_match, name]	
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


files = os.listdir(DIR_SRC)

for item1 in files:
	path_src =  os.path.join(DIR_SRC, item1)
	print( path_src)
	code = ''
	name_en = ''
	lat = 0
	lon = 0
	pref_code, name_ja = read_geojson(path_src)
	is_match, name_en = item =find_pref(pref_code, name_ja)
	filename =  FORMAT_FILE_NAME.format(name=name_en)
	path_dst =  os.path.join(DIR_DST, filename)
	shutil.copyfile(path_src, path_dst)
#






