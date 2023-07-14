# screen_overlay.py
# 2023-06-01 K.OHWADA

import simplekml


# Document
DOC_NAME = 'Screen Overlay Demo'
DOC_DESC = 'display Legend: Wetlands at centor of screen'
FILENAME = 'screen_overlay.kml'


# Wetlands
name = 'Legend: Wetlands'
url_icon = 'https://raw.githubusercontent.com/ohwada/World_Countries/master//simplekml/screen_overlay/images/legend_wetlands.jpg'


# create kml
kml = simplekml.Kml()
kml.document.name = DOC_NAME
kml.document.description = DOC_DESC

screen = kml.newscreenoverlay(name=name)
screen.icon.href = url_icon
screen.overlayxy = simplekml.OverlayXY(x=0.5, y=0.5, xunits=simplekml.Units.fraction,
                                       yunits=simplekml.Units.fraction)
screen.screenxy = simplekml.ScreenXY(x=0.5, y=0.5, xunits=simplekml.Units.fraction,
                                     yunits=simplekml.Units.fraction)
screen.size.x = -1
screen.size.y = -1
screen.size.xunits = simplekml.Units.fraction
screen.size.yunits = simplekml.Units.fraction
kml.save(FILENAME)