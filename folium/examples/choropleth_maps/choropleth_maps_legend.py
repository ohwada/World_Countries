# choropleth_maps_legend.py
# 2023-06-01 K.OHWAA

import folium
import pandas as pd

url = (
    "https://raw.githubusercontent.com/python-visualization/folium/main/examples/data"
)

state_geo = f"{url}/us-states.json"
state_unemployment = f"{url}/US_Unemployment_Oct2012.csv"
state_data = pd.read_csv(state_unemployment)

# center of USA
map = folium.Map(location=[48, -102], zoom_start=3)

# sequence of scalars
bins = list(state_data["Unemployment"].quantile([0, 0.25, 0.5, 0.75, 1]))

folium.Choropleth(
    geo_data=state_geo,
    data=state_data,
    columns=["State", "Unemployment"],
    key_on="feature.id",
    fill_color="BuPu",
    fill_opacity=0.7,
    line_opacity=0.5,
    legend_name="Unemployment Rate (%)",
    bins=bins,
    reset=True,
).add_to(map)


map.save('choropleth_maps_legend.html')