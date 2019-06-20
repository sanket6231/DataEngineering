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
