# jlog2html.py
# 2023-06-01 K.OHWADA

import csv


TITLE = '分割されたポリゴンの一覧'

FILE_CSV = 'split_log.csv'

FILE_HTML = 'split_log.html'

FORMAT_A_TAG = '<a href="{href}" target="_blank">{name}</a>'

FORMAT_IMG = '<img src="{src}" decoding="async"  width="{width}" height="{height}" />'

FORMAT_GMAP ='https://www.google.com/maps/@{lat},{lon},{zoom}z'

FORMAT_LATLON = '({lat:.1f}, {lon:.1f})'


ZOOM = 12


def make_coordinates(lat, lon):
    gmap = FORMAT_GMAP.format(lat=lat, lon=lon, zoom=ZOOM)
    latlon =FORMAT_LATLON.format( lat=lat, lon=lon )
    atag =FORMAT_A_TAG.format(href=gmap, name=latlon)
    return atag
#


def make_link(name, url):
    if not url:
        return name
    atag = FORMAT_A_TAG.format(href=url, name=name)
    return atag
#


with open('files/template_html.txt', 'r') as f1:
    template_html = f1.read()
#

with open('files/template_row.txt', 'r') as f2:
    template_row = f2.read()
#

rows = ''


with open(FILE_CSV, 'r') as f3:
    reader = csv.reader(f3)

    for row in reader:
        len_row = len(row)
        print('len: ', len_row)
        if len_row < 6:
            continue
        num = row[0].strip()
        lat = float( row[1].strip() )
        lon = float( row[2].strip() )
        place = row[3].strip()
        display = row[4].strip()
        filename = row[5].strip()

        row_coordinates = make_coordinates(lat, lon)
        row = template_row.format(num=num, place=place, display=display, coordinates=        row_coordinates, filename=filename)
        rows += row
#


html_ref = ''

wdata = template_html.format(body_title=TITLE, reference=html_ref, rows=rows)


with open(FILE_HTML, 'wt') as f4:
    f4.write(wdata)
#

