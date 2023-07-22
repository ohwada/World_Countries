# colorscale3.py
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

# Median_Household_Income : Pure red
colorscale = branca.colormap.linear.PuRd_09.scale(0, 100000)
employed_series = df.set_index("FIPS_Code")["Median_Household_Income_2011"].dropna()


def style_function(feature):
    employed = employed_series.get(int(feature["id"][-5:]), None)
    return {
        "fillOpacity": 0.5,
        "weight": 0,
        "fillColor": "#black" if employed is None else colorscale(employed),
    }


map = folium.Map(location=[48, -102], tiles="cartodbpositron", zoom_start=3)

folium.TopoJson(
    json.loads(requests.get(county_geo).text),
    "objects.us_counties_20m",
    style_function=style_function,
).add_to(map)


map

map.save( 'colorscale3.html')