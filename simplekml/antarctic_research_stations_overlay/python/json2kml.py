# json2kml.py
# 2023-06-01 K.OHWADA

import simplekml
from polycircles import polycircles
import json
import math


FORMAT_DESCRIPTION = '<![CDATA[<a href="{href}">{name}</a>]]>'

# Document1
DOC_NAME1 = 'Research stations in Antarctica with rectangle'
DOC_DESC1 = 'display rectangle at the Coordinates of Research station'
FILENAME1 = 'antarctic_research_stations_rectangle.kml'

# Document2
DOC_NAME2 = 'Research stations in Antarctica with overlay'
DOC_DESC2 = 'display the National Flag at the Coordinates of Research station'
FILENAME2 = 'antarctic_research_stations_overlay.kml'

# South Pole
name= 'South Pole'
lat_pole = -89.0
lon_pole = 0.0
radius = 50000 # 50 km


# Amundsen Scott Station
lat_amundsen = -88.0
lon_amundsen = 10.0
rad = math.radians( abs(lat_amundsen) )
lon_deg_amundsen = 360.0/ (40000.0  * math.cos(rad) ) # (deg/km)

WIDTH = 300

# latitude/longitude angle equivalent to 1km
lat_deg = 360.0/ 40000.0   # (deg/km)

# create kml
kml1 = simplekml.Kml()
kml1.document.name = DOC_NAME1
kml1.document.description = DOC_DESC1

kml2 = simplekml.Kml()
kml2.document.name = DOC_NAME2
kml2.document.description = DOC_DESC2

# display south pole
polycircle = polycircles.Polycircle(latitude=lat_pole, longitude=lon_pole, radius=radius,  number_of_vertices=36)

polygon1 = kml1.newpolygon(name=name, outerboundaryis=polycircle.to_kml())
polygon1.style.polystyle.color = simplekml.Color.changealphaint(200, simplekml.Color.blue)

polygon2 = kml2.newpolygon(name=name, outerboundaryis=polycircle.to_kml())
polygon2.style.polystyle.color = simplekml.Color.changealphaint(200, simplekml.Color.blue)


with open('antarctic_research_stations_coordinates.json') as f1:
    dic1 = json.load(f1)
    list_stations = dic1['stations']
#


# Placemark
for item in list_stations:
	station = item['station']
	url_station = item['url_station']
	url_country_flag = item['url_country_flag']
	country_flag_width = item['country_flag_width']
	country_flag_height = item['country_flag_height']
	lat = item['lat']
	lon = item['lon']
	print(station)

# latitude/longitude angle equivalent to 1km
	rad = math.radians( abs(lat) )
	lon_deg = 360.0/ (40000.0  * math.cos(rad) ) # (deg/km)
	height = int( (WIDTH * country_flag_height) / country_flag_width )

	south = lat 
	west = lon
	north = lat + (height * lat_deg )
	east = lon + ( WIDTH * lon_deg )

# Amundsen Scott Station
	if lat < -89.0:
		height = int( (WIDTH * country_flag_height) / country_flag_width )
		south = lat_amundsen
		west = lon_amundsen
		north = south + ( 	height * lat_deg )
		east = west + ( WIDTH * lon_deg_amundsen )
 
# display rectabgle
	linestring = kml1.newlinestring(name=station)
	linestring.coords = [(west, south), (west, north), (east, north), (east, south), (west, south)]
	linestring.linestyle.width = 2
	linestring.linestyle.color = simplekml.Color.red

# display flag
	ground = kml2.newgroundoverlay(name=station)
	ground.icon.href = url_country_flag
	ground.latlonbox.north = north
	ground.latlonbox.south =  south
	ground.latlonbox.east =  east
	ground.latlonbox.west = west
#

kml1.save(FILENAME1)
kml2.save(FILENAME2)

