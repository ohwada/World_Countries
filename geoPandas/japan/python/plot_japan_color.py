# plot_japan_color.py
# 2023-06-01 K.OHWADA
# https://sorabatake.jp/20510/

import geopandas as gpd
import matplotlib.pyplot as plt
import json
import random

FILE_COLOR_JSON = 'data/web_colors_100.json'


jpnShp = gpd.read_file('japanSHP/gadm36_JPN_1.shp')

print( jpnShp.head() )


with open(FILE_COLOR_JSON, 'r') as f1:
    dic = json.load(f1)
#

list_colors = dic['colors']

len_shp = len( jpnShp)

len_list = len( list_colors)

colors = []

for num in range(len_shp):
	rint = random.randint(0, (len_list -1) )
	item = list_colors[rint]
	color = item['hex']
	print(color)
	colors.append(color) 
#

print(colors)

# ax = jpnShp.plot(figsize=(10, 10))
# jpnShp.plot(ax=ax)

jpnShp.plot(color=colors)

plt.show()
