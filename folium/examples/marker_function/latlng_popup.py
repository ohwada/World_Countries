# latlng_popup.py
# 2023-06-01 K.OHWAA

import folium


# Mount St. Helens
map = folium.Map(location=[46.1991, -122.1889], zoom_start=13)

map.add_child(folium.LatLngPopup())


map.save('latlng_popup.html')
