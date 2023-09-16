# dissolve.py
# 2023-06-01 K.OHWADA


import os
import requests
import urllib.parse
import geopandas as gpd
import matplotlib.pyplot as plt
import shapely
import json

FILE_CITY_LIST = 'data/japan_ordinance_designated_city_list.json'

FILE_GEOJSON = 'wards.geojson'

DIR = 'geojson_cities'

if not os.path.isdir(DIR):
    os.mkdir(DIR)

with open(FILE_CITY_LIST, 'r') as f1:
    dic1 = json.load(f1)
#

list_cities = dic1['cities']


gdf = gpd.read_file(FILE_GEOJSON)

print( gdf.head() )

renamed_gdf = gdf.rename(
    columns={
        "N03_001": "prefecture",
        "N03_002": "bureau",
        "N03_003": "parent_city",
        "N03_004": "child_city",
        "N03_007": "city_id"
    }
)

print( 'renamed_gdf' )

print( renamed_gdf.head() )


for item in list_cities:
    name = item['name']
    name_ja = item['name_ja']
    print(name_ja)
    target_gdf = renamed_gdf[renamed_gdf["parent_city"]==  name_ja]
    print(  target_gdf.head() )

    try:
        grouped_gdf =  target_gdf.dissolve(by=["prefecture", "parent_city"], as_index=False)
    except shapely.errors.GEOSException as error:
        print(error)
        continue
    parent_city_gdf = grouped_gdf[["parent_city", "prefecture", "geometry"]].rename(
    columns={"parent_city": "city"}
)
    print(parent_city_gdf)
    filename = name + '.geojson'
    savepath = os.path.join(DIR, filename)
    parent_city_gdf.to_file(savepath, driver='GeoJSON')
#


