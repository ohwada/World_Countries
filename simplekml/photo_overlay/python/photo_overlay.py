#  photo_overlay.py
# 2023-06-01 K.OHWADA

#  https://simplekml.readthedocs.io/en/latest/overlays.html#photooverlay

import simplekml

# Document
DOC_NAME = 'photooverlay demo'
DOC_DESC = 'display Photo Marker at Yokohama Stadium, Japan'
FILENAME = 'photo_overlay.kml'

# Yokohama Stadium
name = 'Yokohama Stadium'
lat = 35.443428
lon = 139.6401
url_photo = 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/YokohamaStadium_view_%28cropped%29.jpg/320px-YokohamaStadium_view_%28cropped%29.jpg'

# Icon
url_icon ='http://maps.google.com/mapfiles/kml/shapes/camera.png'

# create kml
kml = simplekml.Kml()
kml.document.name = DOC_NAME
kml.document.description = DOC_DESC

photo = kml.newphotooverlay(name=name)
photo.camera = simplekml.Camera(longitude=lon, latitude=lat, altitude=50,
                                altitudemode=simplekml.AltitudeMode.clamptoground)
photo.point.coords = [(lon, lat)]
photo.style.iconstyle.icon.href = url_icon
photo.icon.href = url_photo
photo.viewvolume = simplekml.ViewVolume(-25,25,-15,15,1)
kml.save(FILENAME)