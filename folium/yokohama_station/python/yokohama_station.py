# yokohama_station.py
# 2023-06-01 K.OHWAA

import folium


# Yokohama Station
name = 'Yokohama Station'
lat = 35.465833
lon = 139.622778
ZOOM = 15
FILENAME = 'yokohama_station.html'


FORMAT_TITLE = '''
             <h3 align="center">{}</h3>
             '''

title_html = FORMAT_TITLE.format(name)

# center(Yokohama Station)
map = folium.Map(location=[lat, lon], zoom_start=ZOOM)

# add title
map.get_root().html.add_child(folium.Element(title_html))

# marker(yokohama Station)
folium.Marker(location=[lat, lon], popup=name).add_to(map)

# save html file
map.save(FILENAME)

