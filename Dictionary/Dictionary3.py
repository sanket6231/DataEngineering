# a Python script to concatenate following dictionaries to create a new one.

# Initialize the dictionaries
dict1 = {1: 10, 2: 20}
dict2 = {3: 30, 4: 40}
dict3 = {5: 50, 6: 60}

# Initialize empty dictionary
dict4 = {}

# Add all dictionaries into empty dictionary
dict4.update(dict1)
dict4.update(dict2)
dict4.update(dict3)

print(dict1)
print(dict2)
print(dict3)
print(dict4)
