#!/usr/bin/env python

import sys

params = sys.argv[1:]

if len(params) != 2 :
    print(None)
else :
    first = int(sys.argv[1])
    second = int(sys.argv[2])
    if first<second :
        array = [i for i in range(first, second+1)]
        print(array)
    else :
        print(None)