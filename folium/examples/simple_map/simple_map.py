# simple_map.py
# 2023-06-01 K.OHWAA

# https://python-visualization.github.io/folium/quickstart.html

import folium

# Portland, Oregon
map = folium.Map(location=[45.5236, -122.6750])

map.save('simple_map.html')
