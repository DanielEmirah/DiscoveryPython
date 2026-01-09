#!/usr/bin/env python

def famous_births(d):
    sorted_d = sorted(d.values(), key=lambda x : int(x["date_of_birth"]))
    for s in sorted_d:
        print(f"{s["name"]} is a great scientist born in {s["date_of_birth"]}")


women_scientists = {
    "ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
    "cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
    "lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
    "grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}

famous_births(women_scientists)
