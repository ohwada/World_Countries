Custom Tileset
===============

display Map using custom tileset

### Map Tilesets

[folium: Map](https://python-visualization.github.io/folium/modules.html#folium.folium.Map)

Generate a base map of given width and height with either default tilesets or a custom tileset URL. 

###  Builtin Tilesets

The following tilesets are built-in to Folium. Pass any of the following to the “tiles” keyword:

default "OpenStreetMap"

-“OpenStreetMap”
-“Mapbox Bright” (Limited levels of zoom for free tiles)
-“Mapbox Control Room” (Limited levels of zoom for free tiles)
-“Stamen” (Terrain, Toner, and Watercolor)
-“Cloudmade” (Must pass API key)
-“Mapbox” (Must pass API key)
-“CartoDB” (positron and dark_matter)

Python  
- stamen_tile.py
tile of "Stamen Terrain"

###  Custom Tileset

You can pass a custom tileset to Folium by passing a xyzservices.

TileProvider or a Leaflet-style URL to the tiles parameter: 
http://{s}.yourtiles.com/{z}/{x}/{y}.png.

You can find a list of free tile providers here: 
http://leaflet-extras.github.io/leaflet-providers/preview/. 

Be sure to check their terms and conditions and to provide attribution with the attr keyword.

python  
- gsi_tile.py
tile of GSI( Geospatial Information Authority of Japan )


