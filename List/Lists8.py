# Python program to find the list of words that are longer than n from a
# given list of words.

list1 = ['Hii', 'Hello', 'What', 'Why', 'When', 'How']
n = 3
for list_item in list1:
    if len(list_item) <= n:
        list1.remove(list_item)

print(list1)
