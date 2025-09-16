def find_the_redheads(family):
    return list(filter(lambda name: family[name] == "red", family))

dupont_family = {
    "Somsak": "red",
    "Somkid": "blond",
    "Somchiay": "brunette",
    "Somying": "red",
    "Somsamai": "red"
}

print(find_the_redheads(dupont_family))
