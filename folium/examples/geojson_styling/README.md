GeoJSON Styling
===============

Styling function

GeoJson and TopoJson features accepts style_function to allow for further custimization of the map. 

(1) download "us_counties_20m_topo.json"
set colorscale

(2) display  center of USA [Wabek, North Dakota](https://en.wikipedia.org/wiki/Wabek,_North_Dakota)
with cartodbpositron(monotone)

(3) apply colorscale

using
[TopoJson](https://python-visualization.github.io/folium/modules.html#folium.features.TopoJson)

Creates a TopoJson object for plotting into a Map.


There are Three typs of Python programs different Styles

- colorscale1.py  
Employed : Yellow or Red   
- colorscale2.py  
Unemployment_rate : Yellow Green Blue   
- colorscale3.py  
Median_Household_Income : Pure Red 

![colormap1](https://github.com/ohwada/World_Countries/blob/main/folium/examples/geojson_styling/screenshots/colormap1.png)
