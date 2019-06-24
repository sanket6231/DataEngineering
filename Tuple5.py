tuple1 = (1, 2, 3, 4, 5, 6, 2, 6, 4, 7, 3)
result_list = []

for ele in tuple1:
    if tuple1.count(ele) > 1:
        if ele not in result_list:
            result_list.append(ele)

tuple2 = tuple(result_list)
print('Repeated elements are -> ', tuple2)
