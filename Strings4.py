string = input('Enter the string -> ')
if len(string) > 3:
    if string[len(string)-3:] == 'ing':
        print(string + 'ly')
    else:
        print(string + 'ing')
else:
    print('Length of the string should be greater than 3..')

