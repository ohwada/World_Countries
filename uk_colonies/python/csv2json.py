# csv2json.py
# 2023-06-01 K.OHWADA

import csv
import json

dic = {}

dic['title'] = "List of countries that have gained independence from the United Kingdom"

dic['desc'] ="Below are lists of the countries and territories formerly ruled or administered by the United Kingdom or part of the British Empire (including military occupations that did not retain the pre-war central government), with their independence days. Some countries did not gain their independence on a single date, therefore the latest day of independence is shown with a break down of dates further down. A total of 65 countries have claimed their independence from the British Empire or the United Kingdom."

dic['reference'] = "wikipedia: List of countries that have gained independence from the United Kingdom"

dic['url_reference'] ="https://en.wikipedia.org/wiki/List_of_countries_that_have_gained_independence_from_the_United_Kingdom"

countries=[]

with open('uk_colonies.csv') as f1:
    reader = csv.reader(f1)
    for row in reader:
        d= {}
        d['country'] = row[0].strip()
        d['url_country'] = row[1].strip()
        d['pre_name'] = row[2].strip()
        d['date'] = row[3].strip()
        d['year'] = int( row[4].strip() )
        d['notes'] = row[5].strip()

        print(d)
        countries.append(d)

dic['countries'] = countries

with open('uk_colonies.json', 'wt') as f2:
    json.dump(dic, f2)
