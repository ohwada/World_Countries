# colorscale1.py
# 2023-06-01 K.OHWAA

import folium
import json
import requests
import branca
import pandas as pd


url = (
    "https://raw.githubusercontent.com/python-visualization/folium/main/examples/data"
)
county_data = f"{url}/us_county_data.csv"
county_geo = f"{url}/us_counties_20m_topo.json"


df = pd.read_csv(county_data, na_values=[" "])

# Employed : Yellow or Red
colorscale = branca.colormap.linear.YlOrRd_09.scale(0, 50e3)
employed_series = df.set_index("FIPS_Code")["Employed_2011"]


def style_function(feature):
    employed = employed_series.get(int(feature["id"][-5:]), None)
    return {
        "fillOpacity": 0.5,
        "weight": 0,
        "fillColor": "#black" if employed is None else colorscale(employed),
    }

# center of USA
map = folium.Map(location=[48, -102], tiles="cartodbpositron", zoom_start=3)

folium.TopoJson(
    json.loads(requests.get(county_geo).text),
    "objects.us_counties_20m",
    style_function=style_function,
).add_to(map)


map.save('colorscale1.html')