#!/usr/bin/env python

age = int(input("Please tell me your age : "))
years_diff = 10

print(f"You are currently {age} years old.")

while years_diff <= 30:
    print(f"In {years_diff} years, you'll be {age+years_diff} years old.")
    years_diff += 10