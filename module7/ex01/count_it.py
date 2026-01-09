#!/usr/bin/env python

import sys

if len(sys.argv) == 1 :
    print(None)
else :
    params = sys.argv[1:]
    for p in params :
        print(f"{p} : {len(p)}")