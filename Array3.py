# Python program to get the number of occurrences of a specified element in an array.

from array import *

# Initialize the array
arr = array('i', [10, 20, 30, 40, 50, 60, 70, 10, 40])
# Get the element value from user
get_element = int(input('Enter the number -> '))
# Print the output
print(arr.count(get_element))
