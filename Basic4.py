function_name = ""

while function_name != 'quit':
    function_name = input('Enter Function Name -> ').lower()
    if function_name == 'quit':
        break
    elif function_name == 'abs()':
        print(abs.__doc__)
    elif function_name == 'cmp()':
        print(cmp.__doc__)
    elif function_name == 'max()':
        print(max.__doc__)
    elif function_name == 'min()':
        print(min.__doc__)
else:
    print('There is no such function found')
