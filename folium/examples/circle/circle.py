# circle.py
# 2023-06-01 K.OHWAA

# https://python-visualization.github.io/folium/quickstart.html


import folium

# Portland, Oregon
map = folium.Map(location=[45.5236, -122.6750], zoom_start=13)

# Waterfront (crimson)
folium.Circle(
    radius=100,
    location=[45.5244, -122.6699],
    popup="The Waterfront",
    color="crimson",
    fill=False,
).add_to(map)

# Laurelhurst Park (blue)
folium.CircleMarker(
    location=[45.5215, -122.6261],
    radius=50,
    popup="Laurelhurst Park",
    color="#3186cc",
    fill=True,
    fill_color="#3186cc",
).add_to(map)


map.save('circle.html')
