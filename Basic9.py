# Python program to concatenate all elements in a list into a string and return it.


def list_to_string(list_of_letters):
    string = ''
    for item in list_of_letters:
        string += item
    return string


list_of_letters = ['H', 'E', 'L', 'L', 'O', ' ', 'W', 'O', 'R', 'L', 'D']
string_of_word = list_to_string(list_of_letters)


print(string_of_word)
