choropleth maps
===============

Choropleth maps

Choropleth can be easily created by binding the data between Pandas DataFrames/Series and Geo/TopoJSON geometries. 
Color Brewer sequential color schemes are built-in to the library, and can be passed to quickly visualize different combinations.

[wikipedia: Choropleth map](https://en.wikipedia.org/wiki/Choropleth_map)

(1) display center of USA

(2) download "us-states.json"
and plot Choropleth map

using [folium: Choropleth](https://python-visualization.github.io/folium/modules.html#folium.features.Choropleth)

Python
- choropleth_maps.py

![choropleth_maps](https://github.com/ohwada/World_Countries/blob/main/folium/examples/choropleth_maps/screenshots/choropleth_maps.png)


### The legend

The legend on the upper right is automatically generated for your values using 6 same sized bins. 
Passing your own bins (number or list) is simple:

Python
- choropleth_maps_legend.py
