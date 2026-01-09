#!/usr/bin/env python

# def find_the_redheads(d):
#     filter_red = [x for x, y in d.items() if y == "red"]
#     return filter_red

def find_the_redheads(d): 
    filter_red = filter(lambda x : d[x]=="red", d.keys())
    return list(filter_red)

dupont_family = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red"
}
print(find_the_redheads(dupont_family))