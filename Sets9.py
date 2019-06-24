set1 = {1, 2, 3, 4, 5}
set2 = {1, 2, 3}

set3 = set1.symmetric_difference(set2)
set4 = set2.symmetric_difference(set1)
print('Set1 ^ Set2 -> ', set3)
print('Set2 ^ Set1 -> ', set4)
