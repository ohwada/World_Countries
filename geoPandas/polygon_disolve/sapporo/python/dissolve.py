# dissolve.py
# 2023-06-01 K.OHWADA


import os
import requests
import urllib.parse
import geopandas as gpd
import matplotlib.pyplot as plt
import shapely
import json

FILE_SRC = 'sapporo_wards.geojson'

FILE_DST = 'sapporo.geojson'

PARENT = '札幌市'

gdf = gpd.read_file(FILE_SRC)

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

# extract records for Sapporo city
target_gdf = renamed_gdf[renamed_gdf["parent_city"]== PARENT]

grouped_gdf =  target_gdf.dissolve(by=["prefecture", "parent_city"], as_index=False)

parent_city_gdf = grouped_gdf[["parent_city", "prefecture", "geometry"]].rename(
    columns={"parent_city": "city"}
)

print(parent_city_gdf)

parent_city_gdf.to_file(FILE_DST, driver='GeoJSON')



