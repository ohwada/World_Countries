# json2kml.py
# 2023-06-01 K.OHWADA

import simplekml
import json
import math

# Document1
DOC_NAME1 = 'Member states of the United Nations with rectangle'
DOC_DESC1 = 'display rectangle at the Coordinates of the capital'
FILENAME1 = 'un_member_states_rectangle.kml'

# Document2
DOC_NAME2 = 'Member states of the United Nations with overlay'
DOC_DESC2 = 'display the National Flag at the Coordinates of the capital'
FILENAME2 = 'un_member_states_overlay.kml'

WIDTH = 200

# latitude/longitude angle equivalent to 1km
lat_deg = 360.0/ 40000.0   # (deg/km)


# create kml
kml1 = simplekml.Kml()
kml1.document.name = DOC_NAME1
kml1.document.description = DOC_DESC1

kml2 = simplekml.Kml()
kml2.document.name = DOC_NAME2
kml2.document.description = DOC_DESC2


with open('un_members_capital.json') as f1:
    dic = json.load(f1)
    list_countries = dic['countries']
#


# Placemark
for item in list_countries:
	country = item['country']
	url_flag = item['url_flag']
	flag_width = item['flag_width']
	flag_height = item['flag_height']
	lat = item['lat']
	lon = item['lon']
	print(country)

# latitude/longitude angle equivalent to 1km
	rad = math.radians( abs(lat) )
	lon_deg = 360.0/ (40000.0  * math.cos(rad) ) # (deg/km)

# image height
	height = int( (WIDTH * flag_height) / flag_width )

	south = lat 
	west = lon
	east = lon + ( WIDTH * lon_deg )
	north = lat + ( height * lat_deg )

# display rectabgle
	linestring = kml1.newlinestring(name=country)
	linestring.coords = [(west, south), (west, north), (east, north), (east, south), (west, south)]
	linestring.linestyle.width = 2
	linestring.linestyle.color = simplekml.Color.red

# display flag
	ground = kml2.newgroundoverlay(name=country)
	ground.icon.href = url_flag
	ground.latlonbox.north = north
	ground.latlonbox.south =  south
	ground.latlonbox.east =  east
	ground.latlonbox.west = west
#

kml1.save(FILENAME1)
kml2.save(FILENAME2)

