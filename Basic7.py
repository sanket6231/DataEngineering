numbers = [1, 6, 3, 5, 74, 1]
try:

    get_number = int(input('Enter Number -> '))

    if get_number in numbers:
        print('True')
    else:
        print('False')
except ValueError as e:
    print (e)
