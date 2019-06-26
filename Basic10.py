# Python program to print out a set containing all the colors from color_list_1 which
# are not present in color_list_2.


def Diff_list(list1, list2):
    result = []
    for l1 in list1:
        if l1 not in list2:
            result.append(l1)
    return result


color_list1 = ["White", "Black", "Red"]
color_list2 = ["Red", "Green"]
result = Diff_list(color_list1, color_list2)
print (result)
