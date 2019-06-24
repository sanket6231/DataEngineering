list1 = ['abc', 'xyz', 'aba', '1221', 'asdffdsa']
result = 0
for list_item in list1:
    if len(list_item) > 2:
        if list_item[0] == list_item[len(list_item) - 1]:
            result += 1

print(result)
