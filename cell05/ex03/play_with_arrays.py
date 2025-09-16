original_array = [2, 8, 9, 48, 8, 22, -12, 2]
new_set = set()

for num in original_array:
    if num > 5:
        value = num + 2
        new_set.add(value)

new_array = list(new_set)

print(original_array)
print(new_array)
