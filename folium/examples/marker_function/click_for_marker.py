# click_for_marker.py
# 2023-06-01 K.OHWAA

import  folium


FILENAME = 'click_for_marker.html'

# Mount Rainier
map = folium.Map(location=[46.8527, -121.7649], zoom_start=13)

# Camp Muir
folium.Marker([46.8354, -121.7325], popup="Camp Muir").add_to(map)

map.add_child(folium.ClickForMarker(popup="Waypoint"))


map.save('click_for_marker.html')