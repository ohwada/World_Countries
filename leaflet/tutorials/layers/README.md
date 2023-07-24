 Layers
===============

Extending Leaflet: Layers

How to extend layers or create new ones, using specific entry points for doing so.

[Extension methods](https://leafletjs.com/examples/extending/extending-2-layers.html)

A few of the Leaflet classes have so-called “extension methods”: entry points for writing code for sub-classes.

One of them is L.TileLayer.getTileUrl(). This method is called internally by L.TileLayer whenever a new tile needs to know which image to load. By making a subclass of L.TileLayer and rewriting its getTileUrl() function, we can create custom behaviour.

Let’s illustrate with a custom L.TileLayer that will display random kitten images from 
[PlaceKitten](https://placekitten.com/)

![layers]()

