# tokyo_japan_flag.py
# 2023-06-01 K.OHWADA

import simplekml


# Document
DOC_NAME = 'Tokyo Japan'
DOC_DESC = 'display the Japanese National Flag atTokyo Japan'
FILENAME = 'tokyo_japan_flag.kml'


# Placemark
name = 'Tokyo, Japan'
lat = 35.689722
lon = 139.692222
url_flag = 'https://raw.githubusercontent.com/ohwada/World_Countries/master/simplekml/tokyo_japan_flag/images/100px-Flag_of_Japan.png'


# create kml
kml = simplekml.Kml()
kml.document.name = DOC_NAME
kml.document.description = DOC_DESC
point = kml.newpoint(name = name)
point.coords = [(lon, lat)]
point.style.iconstyle.icon.href = url_flag
kml.save(FILENAME)

