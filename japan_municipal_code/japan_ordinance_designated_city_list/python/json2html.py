# json2html.py
# 2023-06-01 K.OHWADA

import json

FILE_JSON = 'japan_ordinance_designated_city_list.json'

FILE_HTML = 'japan_ordinance_designated_city_list.html'


LF_HTML = '&#010;'

BR = '<br/>'

def  replace_lf(data):
    if not data:
        return ""
    ret = data.replace(LF_HTML,  BR)
    return ret
#


FORMAT_A_TAG = '<a href="{href}">{name}</a>'


with open('template_html.txt', 'r') as f1:
    template_html = f1.read()
#

with open('template_row.txt', 'r') as f2:
    template_row = f2.read()
#

rows = ''

with open(FILE_JSON) as f3:
    dic = json.load(f3)
#

title_ja = dic['title_ja']
ref = dic['reference']
url_ref = dic['url_reference']
list_cities = dic['cities']


for item in list_cities :
    name = item['name']
    name_ja = item['name_ja']
    population = item['population']
    date = item['date']
    decree = replace_lf( item['decree'] )

    row = template_row.format(name=name, name_ja=name_ja, population=population, date =date, decree=decree)
    print(row)
    rows +=  row
#


html_ref = FORMAT_A_TAG.format(href=url_ref, name=ref)

wdata = template_html.format(body_title=title_ja, reference=html_ref, rows=rows)
  
with open(FILE_HTML, 'wt') as f4:
    f4.write(wdata)
#

