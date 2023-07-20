# south_pole.py
# 2023-06-01 K.OHWADA

import simplekml
from polycircles import polycircles

# Document
DOC_NAME = 'south pole'
DOC_DESC = 'display circle at South pole'
FILENAME = 'south_pole.kml'


# circle
name= 'South Pole'
lat = -89.0
lon = 0.0
radius = 100000 # 100 km


# create kml
kml = simplekml.Kml()
kml.document.name = DOC_NAME
kml.document.description = DOC_DESC
polycircle = polycircles.Polycircle(latitude=lat, longitude=lon, radius=radius,  number_of_vertices=36)
polygon = kml.newpolygon(name=name, outerboundaryis=polycircle.to_kml())
polygon.style.polystyle.color = simplekml.Color.changealphaint(200, simplekml.Color.blue)
kml.save(FILENAME)

