dicts = {'a': 1, 'b': 12, 'c': 32, 'd': 4, 'e': 50}

list_items = [(k, v) for v, k in dicts.items()]
list_items.sort()
print('Ascending Sorting -> ', list_items)
list_items.reverse()
print('Descending Order ->', list_items)
