# plot_sapporo_wards.py
# 2023-06-01 K.OHWADA

import geopandas as gpd
import matplotlib.pyplot as plt
import json
import random


FILE_COLOR_JSON = 'data/web_colors_100.json'

DATA_FILE_NAME = "sapporo_wards.geojson"

with open(FILE_COLOR_JSON, 'r') as f1:
    dic = json.load(f1)
#

list_colors = dic['colors']


gdf = gpd.read_file(DATA_FILE_NAME)

print( gdf )

len_gdf = len(gdf)

colors = []

for num in range(len_gdf):
	rint = random.randint(0, (len_gdf -1) )
	item = list_colors[rint]
	color = item['hex']
	print(color)
	colors.append(color) 
#

print(colors)

gdf.plot(color=colors)

plt.show()
