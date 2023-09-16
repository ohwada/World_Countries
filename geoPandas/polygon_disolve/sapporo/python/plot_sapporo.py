# plot_sapporo.py
# 2023-06-01 K.OHWADA

import geopandas as gpd
import matplotlib.pyplot as plt

DATA_FILE_NAME = "sapporo.geojson"
gdf = gpd.read_file(DATA_FILE_NAME)

print( gdf )

gdf.plot()
plt.show()
