# polygon.py
# 2023-06-01 K.OHWADA

import simplekml


# Document
DOC_NAME = 'polygon demo'
DOC_DESC = 'display polygon'
FILENAME = 'polygon.kml'


# polygon
name = 'Yokohama, Saitame,  Narita'
# Yokohama 
lat1 = 35.45033
lon1 = 139.63422
# Saitame
lat2 = 35.8614
lon2 = 139.6456
# Narita
lat3 = 35.7767
lon3 =140.3183
# Kawasaki
lat4 = 35.53089
lon4 =139.703
# Kawaguchi
lat5 = 35.80758
lon5 = 139.72414
# Ichikawa
lat6 = 35.72192
lon6 = 139.93106


# create kml
kml = simplekml.Kml()
kml.document.name = DOC_NAME
kml.document.description = DOC_DESC
pol = kml.newpolygon(name=name)
pol.outerboundaryis = [(lon1, lat1), (lon2, lat2), (lon3, lat3), (lon1, lat1)]
pol.innerboundaryis = [(lon4, lat4), (lon5, lat5), (lon6, lat6), (lon4, lat4)]
pol.style.linestyle.color = simplekml.Color.green
pol.style.linestyle.width = 5
pol.style.polystyle.color = simplekml.Color.changealphaint(100, simplekml.Color.green)
kml.save(FILENAME)

