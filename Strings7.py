# Python program that accepts a comma separated sequence of words as input
# and prints the unique words in sorted form (alphanumerically).

string = input('Enter the comma separated string -> ')
if ',' in string:
    print('original string ->', string)
else:
    print('Input string not in correct format..')

get_list = list(string.split(','))
get_list.sort()
get_list = list(dict.fromkeys(get_list))
print('Sorted sting -> ', ','.join(get_list))
