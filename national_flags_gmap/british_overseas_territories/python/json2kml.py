# json2kml.py
# 2023-06-01 K.OHWADA

import simplekml
import json
import urllib.parse

FORMAT_DESCRIPTION = '<![CDATA[<a href="{href}">{name}</a>]]>'

# Document
DOC_NAME = 'British Overseas Territories'
DOC_DESC = 'display the National Flag at the Coordinates of the Capital'
FILENAME = 'british_overseas_territories.kml'

# create kml
kml = simplekml.Kml()
kml.document.name = DOC_NAME
kml.document.description = DOC_DESC

with open('british_overseas_territories_coordinates.json') as f1:
    dic = json.load(f1)
    list_territories = dic['territories']
#


# Placemark
for item in list_territories:
	territory = item['territory']
	url_territory = item['url_territory']
	url_flag = item['url_flag']
	lat = item['lat']
	lon = item['lon']
	print(territory)

	point = kml.newpoint(name = territory)
	point.coords = [(lon, lat)]
	point.style.iconstyle.icon.href = url_flag
	point.description =  FORMAT_DESCRIPTION.format(href=url_territory, name=territory)
#

kml.save(FILENAME)

