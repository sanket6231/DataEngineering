list1 = [234, 65, 87, 32, 10, 431, 5, 6, 13]
small_no = list1[0]
for list_item in list1:
    if small_no > list_item:
        small_no = list_item

print(small_no)
