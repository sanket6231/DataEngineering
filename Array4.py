from array import *

arr = array('i', [10, 20, 30, 40, 50, 60, 70, 10, 40])
print(arr)
get_element = int(input('Enter the element to remove '))
arr.remove(get_element)
print(arr)