list1 = ['abc', 'xyz', 'aba', '1221', 'asdffdsa', 'xyz', 'abc']
list2 = ['abc', 'xyz']


def common_list(list_1, list_2):
    for list_item in list2:
        if list1.count(list_item) > 1:
            result = True
            break
        else:
            result = False
            continue
    return result


result = common_list(list1, list2)
print(result)

