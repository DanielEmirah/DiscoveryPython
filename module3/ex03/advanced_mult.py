#!/usr/bin/env python

i = 0
b = 0

while i <= 10 :
    print(f"Table of {i} : ", end="")
    while b <= 10 :
        print(f"{i*b} ", end="")
        b += 1
    b = 0
    i += 1
    print()