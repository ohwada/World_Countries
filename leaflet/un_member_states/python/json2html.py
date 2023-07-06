# json2html.py
# 2023-06-01 K.OHWADA

import json


with open('template_html.txt', 'r') as f1:
    template_html = f1.read()
#

with open('template_marker.txt', 'r') as f2:
    template_marker = f2.read()
#

with open('leaflet_script.txt', 'r') as f3:
    leaflet_script = f3.read()
#

with open('un_members_capital.json') as f4:
    dic = json.load(f4)
    list_countries = dic['countries']
#


FORMAT_MARKER_LIST = '[{markers}]'

COMMA_SPACE_LF = ', \n'

len_countries = len(list_countries)

cnt = 0

markers = ''

for item in list_countries:
    country = item['country']
    url_country = item['url_country']
    url_flag_icon = item['url_flag_icon']
    icon_width = item['icon_width']
    icon_height = item['icon_height']
    lat = item['lat']
    lon = item['lon']

    marker = template_marker.format(lat=lat, lon=lon, name=country, flag=url_flag_icon, width=icon_width, height=icon_height )

    cnt += 1
    markers += marker
    print(marker)
    if cnt != len_countries:
        markers += COMMA_SPACE_LF
#


marker_list = FORMAT_MARKER_LIST.format(markers=markers)

wdata = template_html.format(marker_list=marker_list, leaflet_script=leaflet_script)
  

with open('leaflet_un_members_with_list.html', 'w') as f5:
    f5.write(wdata)
#

