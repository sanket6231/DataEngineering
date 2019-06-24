tuple = (1, 2, 3, 4, 5)
search_element = 8
try:
    print('The given element is present at index: ', tuple.index(search_element))
except ValueError:
    print('The given element is not present in tuple')
