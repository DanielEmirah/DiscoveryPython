#!/usr/bin/env python

def array_of_names(params):
    nwArray= [f"{x.capitalize()} {y.capitalize()}" for x, y in params.items()]
    return nwArray


persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}

print(array_of_names(persons))