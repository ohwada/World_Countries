# ground_overlay.py

import simplekml
import math

# Document1
DOC_NAME1 = 'simplekml demo'
DOC_DESC1 = 'display rectangle surrounding Mt.Fuji'
FILENAME1 = 'mt_fuji_rectangle.kml'

# Document2
DOC_NAME2 = 'simplekml GroundOverlay demo'
DOC_DESC2 = 'display photo at Mt.Fuji'
FILENAME2 = 'mt_fuji_overlay.kml'

# Mt Fuji
name = 'Mt Fuji'
lat = 35.3606
lon = 138.7275
url_photo = 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/3e/MtFuji_FujiCity.jpg/800px-MtFuji_FujiCity.jpg'

# latitude/longitude angle equivalent to 1km
rad = math.radians(lat)
lat_deg = 360.0/ 40000.0   # (deg/km)
lon_deg = 360.0/ (40000.0  * math.cos(rad) ) # (deg/km)
print('lat_deg: ', lat_deg)
print('on_deg: ', lon_deg)

# rectangle surrounding Mt.Fuji
lon_deg_100 = 100.0 * lon_deg # 100km
lat_deg_50 = 50.0 * lat_deg  # 50km
lat_deg_150 = 150.0 * lat_deg  # 150km
print('lon_deg_100: ', lon_deg_100)
print('lat_deg_150: ', lat_deg_150)

west = lon - lon_deg_100
east = lon + lon_deg_100
south = lat - lat_deg_50
north = lat + lat_deg_150
print('west: ', west)
print('east: ', east)
print('north: ', north)
print('south: ', south)


# create kml1
kml1 = simplekml.Kml()
kml1.document.name = DOC_NAME1
kml1.document.description = DOC_DESC1

linestring = kml1.newlinestring(name=name)
linestring.coords = [(west, south), (west, north), (east, north), (east, south), (west, south)]
linestring.linestyle.width = 2
linestring.linestyle.color = simplekml.Color.red
kml1.save(FILENAME1)


# create kml2
kml2 = simplekml.Kml()
kml2.document.name = DOC_NAME2
kml2.document.description = DOC_DESC2

ground = kml2.newgroundoverlay(name=name)
ground.icon.href = url_photo
ground.latlonbox.north = north
ground.latlonbox.south =  south
ground.latlonbox.east =  east
ground.latlonbox.west = west
kml2.save(FILENAME2)


