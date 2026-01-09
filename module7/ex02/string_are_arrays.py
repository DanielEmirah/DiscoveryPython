#!/usr/bin/env python

import sys
import re

to_find = "z"
params = sys.argv[1]

if len(sys.argv[1:]) != 1 or to_find not in params:
    print(None)
else :
    result = re.findall(to_find, params)
    print("z"*len(result))