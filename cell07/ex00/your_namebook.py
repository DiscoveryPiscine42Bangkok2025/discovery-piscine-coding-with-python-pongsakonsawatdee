def array_of_names(d):
    result = []
    for first, last in d.items():
        full_name = f"{first.capitalize()} {last.capitalize()}"
        result.append(full_name)
    return result

persons = {
    "Suksan": "Jaidee",
    "Boyd": "Kosiyapong",
    "Nop": "Rumphaiphannee",
    "Ink": "Waruntorn"
}

print(array_of_names(persons))
