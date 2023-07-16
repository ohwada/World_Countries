# merge_json.py
# 2023-06-01 K.OHWADA

import json


def find_alias(country):
	is_match = False
	alias = ''
	coop = 0
	if country == 'Ukraine United Kingdom':
		is_match = True
		alias = 'Ukraine'
		coop = 1
	if country == 'Italy France':
		is_match = True
		alias = 'Italy'
		coop = 1
	return [is_match, alias, 	coop]
#


def find_country( list_countries, country, alias):
	for item in  list_countries:
		item_country = item['country']
		item_offical = item['offical_name']

		is_match = False
		if   country == item_country:
			is_match = True
			matched = item
			break		
		if   country == item_offical:
			is_match = True
			matched = item
			break
		if alias == item_country:
			is_match = True
			matched = item
			break
	if is_match:
		return[True, matched]
	else:
		return[False, None]
#


HYPHON = '-'

FORMAT_LINE = '{station}, {url_station}, {url_station_flag}, {station_width}, {station_height}, {location}, {url_location}, {country},{url_country}, {country_coop}, {url_country_icon}, {icon_width}, {icon_height} {url_country_flag}, {flag_width}, {flag_height}, {lat}, {lon} \n'

with open('un_members_flag.json') as f1:
    dic1  = json.load(f1)
#


list_countries = dic1['countries']


with open('antarctic_research_stations.json') as f2:
    dic2 = json.load(f2)
#

list_stations = dic2['stations']

url_station_flag = HYPHON
station_width = 0
station_height = 0
lat = 0
lon =0

wdata = ''


for item in list_stations:
	station = item['station']
	url_station = item['url_station']
	location = item['location']
	url_location = item['url_location']
	country = item['country']
	url_country_flag = item['url_country_flag']
	country_width = item['country_width']
	country_height = item['country_height']
	print(station)

	is_match1, alias, coop =find_alias(country)
	url_country = ''
	url_flag = ''
	flag_width = 0
	flag_height = 0
	is_match2, matched = find_country( list_countries, country, alias )
	if is_match2:
		url_flag = matched['url_flag']
		flag_width = matched['flag_width']
		flag_height = matched['flag_height']
		if coop == 0:
			url_country = matched['url_country']
	else:
		print('abort: ', country)
		exit()

	line = FORMAT_LINE.format( station=station, url_station=url_station, url_station_flag=url_station_flag, station_width=station_width,station_height=station_height, location=location, url_location=url_location, country=country, url_country=url_country,country_coop=coop,  url_country_icon=url_country_flag, icon_width=country_width, icon_height=country_height, url_country_flag=url_flag, flag_width=flag_width, flag_height=flag_height, lat=lat, lon=lon )
	print(line)
	wdata += line;
#


with open('antarctic_research_stations_coordinates.csv', 'w') as f5:
     f5.write(wdata)
