# Python program which accepts a sequence of comma-separated numbers from user
# and generate a list and a tuple with those numbers.

numbers = input('Enter numbers -> ')

split_numbers = numbers.split(',')

print('List : ', split_numbers)
print('tuple : ', tuple(split_numbers))
