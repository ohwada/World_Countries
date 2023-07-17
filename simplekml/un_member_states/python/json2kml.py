# json2kml_100px.py
# 2023-06-01 K.OHWADA

import simplekml
import json

FORMAT_DESCRIPTION = '<![CDATA[<a href="{href}">{name}</a>]]>'

# Document
DOC_NAME = 'Member states of the United Nations'
DOC_DESC = 'display the National Flag at the Coordinates of the Capital'
FILENAME = 'un_members.kml'

# create kml
kml = simplekml.Kml()
kml.document.name = DOC_NAME
kml.document.description = DOC_DESC

with open('un_members_capital.json') as f1:
    dic = json.load(f1)
    list_countries = dic['countries']
#


# Placemark
for item in list_countries:
	country = item['country']
	url_country = item['url_country']
	url_flag_icon = item['url_flag_icon']
	lat = item['lat']
	lon = item['lon']
	print(country)

	point = kml.newpoint(name = country)
	point.coords = [(lon, lat)]
	point.style.iconstyle.icon.href = url_flag_icon
	point.description =  FORMAT_DESCRIPTION.format(href=url_country, name=country)
#

kml.save(FILENAME)

