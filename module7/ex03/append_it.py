#!/usr/bin/env python

import sys

params = sys.argv[1:]

# for param in params:
#     if param.find('ism') < 0:
#         print(f"{param}ism")

array = []

for param in params:
    if param.find('ism') < 0:
        array.append(param)

for param in array:
    print(f"{param}ism")