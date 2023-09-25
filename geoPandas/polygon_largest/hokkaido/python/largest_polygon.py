# largest_polygon.py

import geopandas as gpd
from shapely import geometry
import json
import os


FILE_PREF_GEOJSON = 'data/hokkaido.geojson'

FILE_OUT = 'hokkaido.geojson'


DIR = 'geojson'


if not os.path.isdir(DIR):
    os.mkdir(DIR)
#


# read geojson file
gdf = gpd.read_file(FILE_PREF_GEOJSON) 

print(gdf)

pref_code = gdf['pref']
pref_name = gdf['name']

# split polygon
df_exploded = gdf.explode(index_parts=True)

print( 'len: ', len(df_exploded) )

# create an array of areas and geometries
area_list = []

for i, row in df_exploded.iterrows():
    geo = row['geometry']
    row['area'] = geo.area
    a = (geo.area, geo)
    area_list.append( a )
#

# sort in descending order of area
sorted_list = sorted(area_list, key=lambda x: x[0], reverse=True)

# select the polygon with the largest area
largest_area = sorted_list[0][0]
largest_poly = sorted_list[0][1]


# convert to GeoDataFrame
df = gpd.GeoDataFrame()
df['geometry'] = None
df.loc[0, 'geometry'] = largest_poly
df['pref'] = pref_code
df['name'] = pref_name

# export to GeoJson file
filepath =  os.path.join(DIR, FILE_OUT)
df.to_file(filepath, driver='GeoJSON')
