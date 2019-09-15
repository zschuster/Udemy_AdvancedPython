dct = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# keys
print(dct.keys())

# values
print(dct.values())

# print out list of key value tuples
print(dct.items())

# more pythonic approach
# values
new_dict_values = {k: v * 2 for (k, v) in dct.items()}
print(new_dict_values)

# keys
new_dict_keys = {k * 2: v for (k, v) in dct.items()}
print(new_dict_keys)

# comparison of for loop vs comprehensions

for_dict = {}
for i in range(10):
	if i % 2 == 0:
		for_dict[i] = i ** 2

print(for_dict)

# comprehension is far more conscise
comp_dict = {i: i ** 2 for i in range(10) if i % 2 == 0}
print(comp_dict)

# dictionary comprehension as lambda functions
feh = {'temp' + str(i): i * 10 for i in range(1, 5)}

# lambda function
cel = list(map(lambda x: (float(5 / 9)) * (x - 32), feh.values()))
cel_dict = dict(zip(feh.keys(), cel))
print(cel_dict)

# dict comprehension
cel_dict = {k: float(5 / 9) * (v - 32) for (k, v) in feh.items()}
print(cel_dict)

# incorporating conditional statements
base_dict = {k: v for (k, v) in zip(['a', 'b', 'c', 'd'], range(1, 5))}

cond_dict = {k: v for (k, v) in base_dict.items() if v >= 3}
print(cond_dict)

cond_dict_2 = {k: 'even' if v % 2 == 0 else 'odd' for (k, v) in base_dict.items()}
print(cond_dict_2)

# nested dictionaries
nested_dict = {'one': {'a': 10}, 'two': {'b': 20}}
print(nested_dict)

# convert numbers into strings
for (external_key, external_value) in nested_dict.items():
	for (internal_key, internal_value) in external_value.items():
		external_value.update({internal_key: str(internal_value)})
print(nested_dict)
