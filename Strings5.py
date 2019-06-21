list_of_word = ['Hi', 'Hello', 'Mumbai', 'India', 'Maharashtra', 'IT']
print(list_of_word)

item_name = ''
item_length = 0

for item in list_of_word:
    if item_length < len(item):
        item_length = len(item)
        item_name = item
print('The longest word in list is -> ', item_name, ' of length ', item_length)
