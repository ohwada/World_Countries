# plot_nakaniikawa.py
# 2023-06-01 K.OHWADA

# https://zenn.dev/spacemarket/articles/012a2a524ec7b8

import geopandas as gpd
import matplotlib.pyplot as plt

DATA_FILE_NAME = "data/N03-21_16_210101.json"
gdf = gpd.read_file(DATA_FILE_NAME)

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

print( renamed_gdf.head() )

has_parent_gdf = renamed_gdf.dropna(subset=["parent_city"])
has_parent_gdf

print(has_parent_gdf)

has_parent_gdf[has_parent_gdf["parent_city"] == "中新川郡"].plot(color=['#FF9800', '#C62828', '#283593'])

plt.show()
