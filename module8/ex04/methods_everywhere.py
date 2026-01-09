#!/usr/bin/env python

import sys

params = sys.argv[1:]

def shrink(word):
    print(word[:8])

def enlarge(word):
    diff = 8-len(word)
    print(word+"Z"*diff)

# shrink("physically")
# enlarge("lol")

for i in params:
    if len(i) == 8:
        print(i)
    elif len(i) > 8:
        shrink(i)
    else :
        enlarge(i)


