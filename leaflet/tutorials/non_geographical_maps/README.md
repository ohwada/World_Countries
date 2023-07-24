Non Geographical Maps
===============

[Not of this earth](https://leafletjs.com/examples/crs-simple/crs-simple.html)

Sometimes, maps do not represent things on the surface of the earth and, as such, do not have a concept of geographical latitude and geographical longitude. 
Most times this refers to big scanned images, such as game maps.

For this tutorial we’ve picked a starmap from Star Control II, a game that is now available as 
[the open-source project The Ur-Quan Masters](https://en.wikipedia.org/wiki/Star_Control_II#The_Ur-Quan_Masters) . 

These maps were made with 
[a tool to read the open-source data files](http://www.highprogrammer.com/alan/games/video/uqm/index.html)
 of the game (webpage seems to have been taken down, 
see 
[the archived version](https://web.archive.org/web/20171112052528/https://www.highprogrammer.com/alan/games/video/uqm/index.html)
), 

and look like this:

![uqm_map](https://leafletjs.com/examples/crs-simple/uqm_map_400px.png)

### CRS.Simple

CRS stands for coordinate reference system, a term used by geographers to explain what the coordinates mean in a coordinate vector. 

For example, [15, 60] represents a point in the Indian Ocean if using latitude-longitude on the earth, or the solar system Krueger-Z in our starmap.

![crs simple](https://github.com/ohwada/World_Countries/blob/main/leaflet/tutorials/non_geographical_maps/screenshots/%20crs_simple.png)

