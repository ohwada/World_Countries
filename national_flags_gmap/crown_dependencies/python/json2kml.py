# json2kml.py
# 2023-06-01 K.OHWADA

import simplekml
import json
import urllib.parse

FORMAT_DESCRIPTION = '<![CDATA[<a href="{href}">{name}</a>]]>'

# Document
DOC_NAME = 'Crown Dependencies'
DOC_DESC = 'display the Flag at the Coordinates of Islands'
FILENAME = 'crown_dependencies.kml'

# create kml
kml = simplekml.Kml()
kml.document.name = DOC_NAME
kml.document.description = DOC_DESC

with open('crown_dependencies_coordinates.json') as f1:
    dic = json.load(f1)
    list_islands = dic['islands']
#


# Placemark
for item in list_islands:
	island = item['island']
	url_island = item['url_island']
	url_flag = item['url_flag']
	lat = item['lat']
	lon = item['lon']
	print(island)

	point = kml.newpoint(name = island)
	point.coords = [(lon, lat)]
	point.style.iconstyle.icon.href = url_flag
	point.description =  FORMAT_DESCRIPTION.format(href=url_island, name=island)
#

kml.save(FILENAME)

