# linestring.py
# 2023-06-01 K.OHWADA

import simplekml


# Document
DOC_NAME = 'linestring demo'
DOC_DESC = 'display blue line'
FILENAME = 'linestring.kml'


# line
name = 'Tokyo to  Osaka'
# Tokyo
lat1 = 35.689722
lon1 = 139.692222
# Osaka
lat2 = 34.69375
lon2 = 135.50211


# create kml
kml = simplekml.Kml()
kml.document.name = DOC_NAME
kml.document.description = DOC_DESC
line = kml.newlinestring(name=name)
line.coords = [(lon1, lat1), (lon2, lat2)]
line.style.linestyle.width = 5
line.style.linestyle.color = simplekml.Color.blue
kml.save(FILENAME)

