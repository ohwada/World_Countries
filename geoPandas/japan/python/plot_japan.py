# plot_japan.py
# 2023-06-01 K.OHWADA
# https://sorabatake.jp/20510/

import geopandas as gpd
import matplotlib.pyplot as plt

jpnShp = gpd.read_file('japanSHP/gadm36_JPN_1.shp')

print( jpnShp.head() )

jpnShp.plot()

plt.show()
