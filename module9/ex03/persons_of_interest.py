#!/usr/bin/env python

def famous_births(d):
    pass


women_scientists = {
    "ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
    "cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
    "lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
    "grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}

# famous_births(women_scientists)

for x in women_scientists:
    name = women_scientists[x]["name"]
    years = women_scientists[x]["date_of_birth"]
    print(f"{name} is a great scientist born in {years}")