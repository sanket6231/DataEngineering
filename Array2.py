from array import *

arr = array('i', [10, 20, 30, 40, 50])
arr.reverse()
print(arr)

# Another Way

arr2 = array('i', [])
max_val = len(arr) - 1
while max_val >= 0:
    arr2.append(arr[max_val])
    max_val -= 1

print(arr2)
