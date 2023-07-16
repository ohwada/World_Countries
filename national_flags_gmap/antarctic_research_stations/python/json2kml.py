# json2kml.py
# 2023-06-01 K.OHWADA

import simplekml
import json
import urllib.parse

FORMAT_DESCRIPTION = '<![CDATA[<a href="{href}">{name}</a>]]>'

# Document
DOC_NAME = 'Research stations in Antarctica'
DOC_DESC = 'display the National Flag at the Coordinates of Research station'
FILENAME = 'antarctic_research_stations.kml'

# create kml
kml = simplekml.Kml()
kml.document.name = DOC_NAME
kml.document.description = DOC_DESC

with open('antarctic_research_stations_coordinates.json') as f1:
    dic = json.load(f1)
    list_stations = dic['stations']
#


# Placemark
for item in list_stations:
	station = item['station']
	url_station = item['url_station']
	url_country_flag_icon = item['url_country_flag_icon']
	lat = item['lat']
	lon = item['lon']
	print(station)

	point = kml.newpoint(name = station)
	point.coords = [(lon, lat)]
	point.style.iconstyle.icon.href = url_country_flag_icon
	point.description =  FORMAT_DESCRIPTION.format(href=url_station, name=station)
#

kml.save(FILENAME)

