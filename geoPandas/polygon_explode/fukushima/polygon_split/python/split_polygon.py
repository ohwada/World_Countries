# split_polygon.py

import geopandas as gpd
from shapely import geometry
from shapely.geometry import Point
import requests
import json
import os


FILE_PREF_GEOJSON = 'data/fukushima.geojson'

FILE_ISLAND_LIST = 'data/fukushima_island_list.json'

FILE_PLACE_LIST = 'data/fukushima_place_list.json'

FILE_CSV  = 'split_log.csv'


FORMAT_URL_REV_GEOCODE =  'https://nominatim.openstreetmap.org/reverse?lat={lat}&lon={lon}&format=json'

FORMAT_NAME_FILENAME = '{name}.geojson'

FORMAT_INDEX_FILENAME = 'place_{cnt: 03d}.geojson'

FROMAT_LINE = '{num}, {lat}, {lon}, {name_place}, {display}, {filename} \n'

COMMA = ','

COMMA_HTML = '&comma;'

DIR = 'geojson'


if not os.path.isdir(DIR):
    os.mkdir(DIR)
#


with open(FILE_ISLAND_LIST, 'r') as f1:
    dic1 = json.load(f1)
#

list_islands = dic1['islands']


with open(FILE_PLACE_LIST, 'r') as f2:
    dic2 = json.load(f2)
#

list_places = dic2['places']


def within(geo):
    is_within = False
    name_en = ''
    name_island = ''
    name_municipality = ''
    for item1 in list_islands:
        name_en = item1['name_en']
        name_island = item1['name_island']
        name_municipality = item1['name_municipality']
        lat = item1['lat']
        lon = item1['lon']
        point = Point(lon, lat)
        if point.within(geo):
            is_within = True
            break
    if is_within:   
        return [is_within, name_en, name_island, name_municipality]

    is_within2 = False
    name_en2 = ''
    name_place2 = ''
    name_municipality2 = ''
    for item2 in list_places:
        name_en2 = item2['name_en']
        name_place2 = item2['name_place']
        name_municipality2 = item2['name_municipality']
        lat2 = item2['lat']
        lon2 = item2['lon']
        point2 = Point(lon2, lat2)
        if point2.within(geo):
            is_within2 = True
            break
    return [is_within2, name_en2, name_place2, name_municipality2]
#


def rev_geocode(lat, lon):
    url = FORMAT_URL_REV_GEOCODE.format(lat=lat, lon=lon)
    res = requests.get(url)
    jobj = json.loads(res.text)
    display = ''
    if  'display_name'  in jobj:
        display_name = jobj['display_name']
        display =  display_name.replace(COMMA, COMMA_HTML)
    return display
#


# read geojson file
gdf = gpd.read_file(FILE_PREF_GEOJSON) 
print(gdf)

pref_name = gdf['name']

df_exploded = gdf.explode(index_parts=True)

print( 'len: ', len(df_exploded) )


cnt = 0

wdata = ''


for i, row in df_exploded.iterrows():
    cnt += 1
    geo = row['geometry']
    df = gpd.GeoDataFrame()
    df['geometry'] = None
    df.loc[0, 'geometry'] = geo
    df['pref'] = pref_name
    # calculate gravity center
    point = geo.centroid
    lat = point.y
    lon= point.x
    print('lat=', lat, ' lon=', lon)
    display = ''
    is_within, name_en, name_place, name_municipality = within(geo)
    if is_within:
        df['place'] =  name_place
        df['municipality'] =  name_municipality
        filename = FORMAT_NAME_FILENAME.format(name=name_en)

    else:
# reverse geocode
        display = rev_geocode(lat, lon)
        print(display)
        filename = FORMAT_INDEX_FILENAME.format(cnt=cnt)
#

# write geojson
    filepath =  os.path.join(DIR, filename)
    df.to_file(filepath, driver='GeoJSON')
# log data
    line = FROMAT_LINE.format(num=cnt, lat=lat, lon=lon, name_place= name_place, display=display, filename=filename)
    print(line)
    wdata += line
# df_exploded.iterrows


with open(FILE_CSV, 'wt') as f3:
    f3.write(wdata)
#
