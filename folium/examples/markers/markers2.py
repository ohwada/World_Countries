# markers2.py
# 2023-06-01 K.OHWAA

# https://python-visualization.github.io/folium/quickstart.html#Markers

import folium

# Portland, Oregon
map = folium.Map(location=[45.372, -121.6972], zoom_start=12)

# Mt. Hood Meadows : "cloud
folium.Marker(
    location=[45.3288, -121.6625],
    popup="Mt. Hood Meadows",
    icon=folium.Icon(icon="cloud"),
).add_to(map)

# Timberline Lodge : Green
folium.Marker(
    location=[45.3311, -121.7113],
    popup="Timberline Lodge",
    icon=folium.Icon(color="green"),
).add_to(map)

# Some Other Location : Red info-sign
folium.Marker(
    location=[45.3300, -121.6823],
    popup="Some Other Location",
    icon=folium.Icon(color="red", icon="info-sign"),
).add_to(map)


map.save( 'markers2.html')
