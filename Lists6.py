def my_function(x):
  return list(dict.fromkeys(x))


list1 = ['abc', 'xyz', 'aba', '1221', 'asdffdsa', 'xyz', 'abc']
mylist = my_function(list1)

print(mylist)
