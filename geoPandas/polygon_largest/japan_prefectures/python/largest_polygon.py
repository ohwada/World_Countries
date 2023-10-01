# largest_polygon.py

import geopandas as gpd
from shapely import geometry
import json
import os


DIR_DOWN = 'geojson_down'

DIR_LARGEST = 'geojson_largest'


def largest_polygon(gdf):
    df_exploded = gdf.explode(index_parts=True)
    area_list = []
    for i, row in df_exploded.iterrows():
        geo = row['geometry']
        a = (geo.area, geo)
        area_list.append( a )
#
    sorted_list = sorted(area_list, key=lambda x: x[0], reverse=True)
    largest_poly =  sorted_list[0][1]

    return largest_poly
#


if not os.path.isdir(DIR_LARGEST):
    os.mkdir(DIR_LARGEST)
#


files = os.listdir(DIR_DOWN)


for item in files:
    filepath1 =  os.path.join(DIR_DOWN, item)
# read geojson file
    gdf = gpd.read_file(filepath1) 
    pref_code = gdf['pref']
    pref_name = gdf['name']
# select the polygon with the largest area
    largest_poly = largest_polygon(gdf)
    df = gpd.GeoDataFrame()
    df['geometry'] = None
    df.loc[0, 'geometry'] = largest_poly
    df['pref'] = pref_code
    df['name'] = pref_name
# write geojson file
    filepath2 =  os.path.join(DIR_LARGEST, item)
    df.to_file(filepath2, driver='GeoJSON')
#
