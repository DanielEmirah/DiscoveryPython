#!/usr/bin/env python

import sys
import re

if len(sys.argv) != 3 or len(re.findall(sys.argv[1].lower(), sys.argv[2].lower())) == 0 :
    print(None)
else :
    print(len(re.findall(sys.argv[1].lower(), sys.argv[2].lower())))