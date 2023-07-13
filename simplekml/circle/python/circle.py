# line.py
# 2023-06-01 K.OHWADA

import simplekml
from polycircles import polycircles

# Document
DOC_NAME = 'circle demo'
DOC_DESC = 'display circle'
FILENAME = 'circle.kml'


# circle
name= 'Nissan Stadium'
lat = 35.510281
lon = 139.606164
radius = 200


# create kml
kml = simplekml.Kml()
kml.document.name = DOC_NAME
kml.document.description = DOC_DESC
polycircle = polycircles.Polycircle(latitude=lat, longitude=lon, radius=radius,  number_of_vertices=36)
polygon = kml.newpolygon(name=name, outerboundaryis=polycircle.to_kml())
polygon.style.polystyle.color = simplekml.Color.changealphaint(50, simplekml.Color.blue)
kml.save(FILENAME)

