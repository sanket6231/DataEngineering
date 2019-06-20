from array import *

arr = array('i', [10, 20, 30, 40, 50, 60, 70])
print('Array : ', arr)

for item in arr:
    print(item)

print('Accessing array elements using index')
try:
    print(arr[0])
    print(arr[1])
    print(arr[2])
    print(arr[3])
    print(arr[4])
except IndexError:
    print('Something went wrong..')
