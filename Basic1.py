# Python program which accepts the user's first and last name and print them in
# reverse order with a space between them.

full_name = input('Enter full name (Fisrtname Lastname) : -> ')
split_name = full_name.split(' ')
print(split_name[1], split_name[0])
