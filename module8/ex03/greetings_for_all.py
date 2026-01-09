#!/usr/bin/env python

# def greetings(name = "noble stranger"):
#     try :
#         number = int(name)
#         print("Error! It was not a name.")
#     except :
#         print(f"Hello, {name}.")

def greetings(name = "noble stranger"):
    if isinstance(name, str):
        print(f"Hello, {name}.")
    else :
        print("Error! It was not a name.")


greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)