# markers1.py
# 2023-06-01 K.OHWAA

# https://python-visualization.github.io/folium/quickstart.html#Markers

import folium

map = folium.Map(location=[45.372, -121.6972], zoom_start=12)

tooltip = "Click me!"

# Mt. Hood Meadows
folium.Marker(
    [45.3288, -121.6625], popup="<i>Mt. Hood Meadows</i>", tooltip=tooltip
).add_to(map)

# Timberline Lodge
folium.Marker(
    [45.3311, -121.7113], popup="<b>Timberline Lodge</b>", tooltip=tooltip
).add_to(map)

map.save('markers1.html')
