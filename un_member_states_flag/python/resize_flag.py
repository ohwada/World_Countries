# resize_flag.py

import os

import json

import re

from urllib.parse import urlparse

import requests

from PIL import Image

FORMAT_FILENAME = '{width}px-{match}.png'

def find_country( list_countries, country):
    for item in  list_countries:
        item_country = item['country']
        is_match = False
        if   country == item_country:
            is_match = True
            matched = item
            break
    if is_match:
        return[True, matched]
    else:
        return[False, None]
#

def parse_filename(url):
	parsed = urlparse(url)
	path = parsed.path
	basename = os.path.basename(path)
	return basename
#

def new_filename(filename, width):
    matched = re.findall('\d+px-(.*).svg.png', filename)
    name = matched[0]
    new_filename = FORMAT_FILENAME.format(width=width, match=name)
    return new_filename
#

COUNTRY = 'Japan'

WIDTH = 100

with open('un_countries_flag.json') as f1:
    dic = json.load(f1)
    list_countries = dic['countries']
    
is_match, item = find_country( list_countries, COUNTRY)
if not is_match:
    print('not mstch')
    exit()

url_flag = item['url_flag']
width = item['flag_width']
height = item['flag_height']
print(url_flag)

filename = parse_filename(url_flag)
print(filename)

data = requests.get(url_flag).content

with open(filename ,mode='wb') as f2:
  f2.write(data)

filename_resize = new_filename(filename, WIDTH)
print(filename_resize)

img = Image.open(filename)

height_resize = int( (WIDTH * height ) / width )

img_resize = img.resize((WIDTH, height_resize))

img_resize.save(filename_resize)
