# Python program to remove the first occurrence of a specified element from an array.

from array import *

# Initialize the array
arr = array('i', [10, 20, 30, 40, 50, 60, 70, 10, 40])
print(arr)
# Get the element value to be removed
get_element = int(input('Enter the element to remove '))
arr.remove(get_element)
print(arr)
