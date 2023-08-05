# parse_topojson.py
# 2023-06-01 K.OHWAA

import os
import json


FILE_PREF_CODE = 'data/japan_pref_code.json'

FILE_CITY_LIST = 'data/japan_ordinance_designated_city_list.json'

FILE_CSV = 'designated_cities.csv'

FORMAT_FILEPATH = '{pref_id}/{name}.topojson'

FORMAT_LINE = '{n001}, {n003}, {n007}, {id}, {filepath}, {name}, {lat}, {lon} \n'


HYPHON = '-'

EMPTY = ''


with open(FILE_PREF_CODE) as f1:
    dic1 = json.load(f1)
#

list_prefectures = dic1['prefectures']


with open(FILE_CITY_LIST) as f2:
    dic2 = json.load(f2)
#

list_designated_cities = dic2['cities']


def find_pref(pref_name):
    is_match = False
    pref_code = ''
    for item in list_prefectures:
        kanji = item['kanji']
        if  kanji == pref_name:
            is_match = True
            pref_code = item['code']
            break
    return [ is_match, pref_code]
#


def find_city(name_ja):
	is_match = False
	matched = None
	name = ''
	lat = 0
	lon = 0
	for item in 	list_designated_cities:
		item_name = item['name']
		item_name_ja = item['name_ja']
		if item_name_ja == name_ja:
			is_match = True
			matched = item
			break
	if is_match:
		name = matched['name']
		lat = matched['lat']
		lon = matched['lon']
	return[is_match, name, lat, lon]
#i


def read_topojson(filepath):
	with open(filepath, 'r') as f:
		dic = json.load(f) 
#
	objects = dic['objects']
	city =   objects['city']
	geometries = city['geometries']
	geometry = geometries[0]
	properties = geometry['properties']
	return properties
#


def make_filepath(pref, id):
    name = id.replace('gci:', EMPTY)
    is_match, pref_id = find_pref(pref)
    filepath= FORMAT_FILEPATH.format(pref_id=pref_id, name=name)
    return filepath
#


def make_line(properties):
	n001 = properties['N03_001']
	n003 = properties['N03_003']
	n007 = properties['N03_007']
	id = properties['id']
	filepath = make_filepath(n001, id)
	is_match, name, lat, lon = find_city(n003)
	line = FORMAT_LINE.format(n001=n001, n003=n003, n007=n007, id=id, filepath=filepath, name=name, lat=lat, lon=lon)
	return line
#


DIR = 'cities'

EXT = '.topojson'

files = os.listdir(DIR)

lines = ''

for item in files:
	root, ext = os.path.splitext(item)
	if ext != EXT:
		continue
	path =  os.path.join(DIR, item)
	properties = read_topojson(path)
	line = make_line(properties)
	print(line)
	lines += line
 #


with open(FILE_CSV, 'wt') as f3:
	f3.write(lines)
#

