# tokyo_japan.py
# 2023-06-01 K.OHWADA

import simplekml


# Document
DOC_NAME = 'Yokohama Japan Icon'
DOC_DESC = 'display Custom Icon at Yokohama Japan'
FILENAME = 'yokohama_japan_icon.kml'


# Placemark
name= 'Yokohama Japan'
lat = 35.45033
lon = 139.63422
url_icon = 'http://maps.google.com/mapfiles/kml/shapes/info-i.png'


# create kml
kml = simplekml.Kml()
kml.document.name = DOC_NAME
kml.document.description = DOC_DESC
point = kml.newpoint(name = name)
point.coords = [(lon, lat)]
point.style.iconstyle.scale = 3  # Icon thrice as big
point.style.iconstyle.icon.href = url_icon
kml.save(FILENAME)

