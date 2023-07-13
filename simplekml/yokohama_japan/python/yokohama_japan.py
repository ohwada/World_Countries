#  yokohama_japan.py
# 2023-06-01 K.OHWADA

import simplekml

# Document
DOC_NAME = 'simplekml demo'
DOC_DESC = 'display Marker at Yokohama Japan'
FILENAME = 'yokohama_japan.kml'

# Placemark
name= 'Yokohama Japan'
lat = 35.45033
lon = 139.63422

# create kml
kml = simplekml.Kml()
kml.document.name = DOC_NAME
kml.document.description = DOC_DESC
point = kml.newpoint(name=name, coords=[(lon, lat)])  # lon, lat, optional height
kml.save(FILENAME)

