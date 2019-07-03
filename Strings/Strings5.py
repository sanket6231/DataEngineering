# Python function that takes a list of words and returns the length of the longest one.

list_of_word = ['Hi', 'Hello', 'Mumbai', 'India', 'Maharashtra', 'IT']
print(list_of_word)


def longest_word(list1):
    item_name = ''
    item_length = 0
    for item in list1:
        if item_length < len(item):
            item_length = len(item)
            item_name = item
    print('The longest word in list is -> ', item_name, ' of length ', item_length)


longest_word(list_of_word)
