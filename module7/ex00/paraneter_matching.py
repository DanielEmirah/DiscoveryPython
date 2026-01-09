#!/usr/bin/env python

import sys

params = sys.argv[1]

if len(sys.argv) != 2 :
    print(None)
else :
    argument = input("What was the parameter? ")
    if params == argument :
        print("Good job!")
    else :
        print("Nope, sorry...")