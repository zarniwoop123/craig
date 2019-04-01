#!/bin/python3

import craigslist
import time
dic = []
a = craigslist.CraigslistHousing(
        site = 'vancouver',
        area = 'van',
        category='roo',
        filters={'max_price': 3000, 'private_room' : True}
        )
for result in a.get_results(sort_by='newest', geotagged=True):
    print(result)
    dic.append(result)
    print(len(dic))
    time.sleep(10)
    print("-" * 150)
    print("\n" * 20)


def getConditions():
    conditions = {}
    print("Enter your requirements:\n")
    print("Max price: ",)
    max_price = input()
    print("Min price: ",)
    min_price = input(
