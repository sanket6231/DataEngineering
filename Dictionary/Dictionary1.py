# Python script to sort (ascending and descending) a dictionary by value.

# Initialize the dictionary
dicts = {'a': 1, 'b': 12, 'c': 32, 'd': 4, 'e': 50}

# Get the dictionary items into list
list_items = [(k, v) for v, k in dicts.items()]
# sort the list. The output will be in ascending order
list_items.sort()
print('Ascending Sorting -> ', list_items)
# Reverse the list. The output will be in descending order
list_items.reverse()
print('Descending Order ->', list_items)
