string = 'restart your brain by taking power nap hehehe'

list_of_words = string.split(' ')
result = ''
for item in list_of_words:
    output = item[0] + item[1:].replace(item[0], '$') + ' '
    result += output
print(result)
