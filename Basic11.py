try:
    number = int(input('Enter a number to convert in binary -> '))
    print('{0:08b}'.format(number))
except ValueError as e:
    print(e)
