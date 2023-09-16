# dissolve.py
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

has_parent_gdf = renamed_gdf.dropna(subset=["parent_city"])
has_parent_gdf

grouped_gdf = renamed_gdf.dissolve(by=["prefecture", "parent_city"], as_index=False)

print(grouped_gdf)

parent_city_gdf = grouped_gdf[["parent_city", "prefecture", "geometry"]].rename(
    columns={"parent_city": "city"}
)

print(parent_city_gdf)

# 中新川郡
nakaniikawa_gdf = parent_city_gdf[parent_city_gdf["city"]=="中新川郡"]

print(nakaniikawa_gdf)

nakaniikawa_gdf.to_file('nakaniikawa.geojson', driver='GeoJSON')


# 下新川郡

shimoniikawa_gdf = parent_city_gdf[parent_city_gdf["city"]=="下新川郡"]

print(shimoniikawa_gdf)

shimoniikawa_gdf.to_file('shimoniikawa.geojson', driver='GeoJSON')

# 中新川郡

nakaniikawa_gdf.plot()
plt.show()




