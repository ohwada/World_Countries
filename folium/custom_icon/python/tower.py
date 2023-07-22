# tower.py
# 2023-06-01 K.OHWAA

import folium


# https://hiyokonoko.com/programming-development-python-folium-icon/1602/

# Yokohama Station
name = 'Yokohama Station'
lat = 35.465833
lon = 139.622778
ZOOM = 15

TITLE = 'Builtin Icon (Tower)'
FILENAME = 'tower.html'

FORMAT_TITLE = '''
             <h3 align="center">{}</h3>
             '''

title_html = FORMAT_TITLE.format(TITLE )


# center(Yokohama Station)
map = folium.Map(location=[lat, lon], zoom_start=ZOOM)


# marker(Yokohama Station)
folium.Marker(
     location = [lat, lon]
     ,popup= name
     ,icon=folium.Icon(icon="tower", icon_color='red', color="green")
).add_to(map)

# add title
map.get_root().html.add_child(folium.Element(title_html))


# save html file
map.save(FILENAME)

