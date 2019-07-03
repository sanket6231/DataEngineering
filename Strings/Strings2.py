# Python program to count the number of characters (character frequency) in a string.

string = 'google.com'
result = {}
for s in string:
    result[s] = string.count(s)
print(result)
