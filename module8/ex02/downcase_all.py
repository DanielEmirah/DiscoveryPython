#!/usr/bin/env python

import sys

def downcase_it(string_var):
    string_low = string_var.lower()
    return string_low

params = sys.argv[1:]

if not params:
    print(None)
else :
    for param in params:
        print(downcase_it(param))