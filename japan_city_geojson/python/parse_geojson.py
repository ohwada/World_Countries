#  parse_geojson.py
# 2023-06-01 K.OHWADA

# require  geojson files
# JapanCityGeoJson 2020
# https://github.com/niiyz/JapanCityGeoJson

import os
import json


FORMAT_LINE = '{filepath}, {n001}, {n002}, {n003}, {n004}, {n007} \n'

FORMAT_FILENAME = 'gepjson_{name}.csv'



def read_json(filepath):
	with open(filepath) as f1:
		dic1 = json.load(f1) 
#
	features = dic1['features']
	feature = features[0]
	properties = feature['properties']
	return properties
#


def make_line( path, properties):
	n001 = properties['N03_001']
	n002 = properties['N03_002']
	n003 = properties['N03_003']
	n004 = properties['N03_004']
	n007 = properties['N03_007']
	line = FORMAT_LINE.format(filepath=path, n001=n001, n002=n002, n003=n003, n004=n004, n007=n007)
	return line
#


def parse_pref_dir(name, path1):
	filename = FORMAT_FILENAME.format(name=name)
	lines = ''
	files = os.listdir(path1)
	for item in files:
		path2 =  os.path.join(path1, item)
		print( path2)
		properties = read_json(path2)
		line = make_line(path2, properties)
		print(line)
		lines += line
 
	with open(filename, 'w') as f2:
		f2.write(lines)
#


dir_path = 'geojson'

dir_files = os.listdir(dir_path)


for item1 in dir_files:
	path1 =  os.path.join(dir_path, item1)
	print( path1)
	isdir = os.path.isdir(path1)
	if isdir:
		pref_name = item1
		print(pref_name)
		parse_pref_dir(pref_name, path1)
#
 


