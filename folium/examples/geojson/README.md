GeoJSON
===============

GeoJSON/TopoJSON Overlays

Both GeoJSON and TopoJSON layers can be passed to the map as an overlay, 
and multiple layers can be visualized on the same map:

overlay Antarctic Ice Edge on Antarctica

(1) download "antarctic_ice_edge.json"

(2) display  Antarctica with 
cartodbpositron(monotone) tiles

(3) plot GeoJson

using
[folium: GeoJson](https://python-visualization.github.io/folium/modules.html#folium.features.GeoJson)

Creates a GeoJson object for plotting into a Map.

![geojson](https://github.com/ohwada/World_Countries/blob/main/folium/examples/geojson/screenshots/geojson.png)

