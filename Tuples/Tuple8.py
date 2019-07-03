# Python program to remove an item from a tuple.

tuple1 = (1, 2, 3, 4, 5, 6, 7)
item_to_be_remove = 4
try:
    converted_list = list(tuple1)
    converted_list.remove(item_to_be_remove)
    tuple1 = tuple(converted_list)
    print(tuple1)
except ValueError:
    print('Item to be remove not present in tuple')
