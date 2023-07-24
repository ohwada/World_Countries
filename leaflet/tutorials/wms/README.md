WMS
===============


[WMS and TMS](https://leafletjs.com/examples/wms/wms.html)

How to integrate with WMS and TMS services from professional GIS software.

WMS, short for 
[web map service](https://en.wikipedia.org/wiki/Web_Map_Service), 
is a popular way of publishing maps by professional GIS software (and seldomly used by non-GISers). 
This format is similar to map tiles, but more generic and not so well optimized for use in web maps. A WMS image is defined by the coordinates of its corners - a calculation that Leaflet does under the hood.

### WMS in Leaflet

When somebody publishes a WMS service, most likely they link to something called a GetCapabilities document. 

For this tutorial, we’ll use the WMS offered by [Mundialis]()https://www.mundialis.de/)

The service capabilities are described at the following URL:

http://ows.mundialis.de/services/service?request=GetCapabilities

[terrestris demos](https://www.terrestris.de/de/demos/)

![wms]()
