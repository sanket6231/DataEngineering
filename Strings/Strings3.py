# Python program to get a string from a given string where all occurrences of its
# first char have been changed to '$', except the first char itself.

string = 'restart your brain by taking power nap hehehe'

list_of_words = string.split(' ')
result = ''
for item in list_of_words:
    output = item[0] + item[1:].replace(item[0], '$') + ' '
    result += output
print(result)
