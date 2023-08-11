# -*- coding: utf-8 -*-
# json2md.py
# 2023-06-01 K.OHWADA

import os
import json
import urllib.parse


FILE_JSON = 'json/japan_prefecture_geojson_catalog.json'

FILE_MD  = 'geojson_list.md'

FORMAT_LINK = '[{name}]({url})'

FORMAT_TITLE = '## {title} \n'

TH = ''''
 | コード | 英語名 | 県名 | ファイル | 
 | --- | --- | --- | --- | 
'''


FORMAT_TD = ' | {code} | {name_en} | {name_ja} | {filepath} | \n'


with open(FILE_JSON, 'r') as f1:
    dic = json.load(f1)
#


title_ja = dic['title_ja']
url_base = dic['url_base']
list_prefectures = dic['prefectures']


wdata = FORMAT_TITLE.format(title=title_ja)
wdata += TH


for item in list_prefectures :
    code = item['code']
    name_en = item['name_en']
    name_ja = item['name_ja']
    filename = item['filename']
    url_geojson = urllib.parse.urljoin(url_base, filename)
    row_filepath = FORMAT_LINK.format(name=filename, url=url_geojson )
    row = FORMAT_TD.format( code=code, name_en=name_en, name_ja=name_ja, filepath=row_filepath )
    print(row)
    wdata +=  row
#


with open(FILE_MD, 'wt') as f4:
    f4.write(wdata)
#

