function_name = ""

while function_name != 'quit':
    function_name = input('Enter Function Name -> ').lower()
    if(function_name == 'quit'):
        break
    elif (function_name == 'abs()'):
        print('''abs(num) -> number
        Returns the absolute value of the argument''')
    elif(function_name == 'ceil()'):
        print('''ceil(x)
        The ceiling of x: the smallest integer not less than x''')
    elif(function_name == 'cmp()'):
        print('''cmp(x, y)
        -1 if x < y, 0 if x == y, or 1 if x > y''')
    elif(function_name == 'exp()'):
        print('''exp(x)
        The exponential of x: ex''')
    elif(function_name == 'fabs()'):
        print('''fabs(x)
        The absolute value of x.''')
    elif(function_name == 'floor()'):
        print('''floor(x)
The floor of x: the largest integer not greater than x''')
    elif(function_name == 'log()'):
        print('''log(x)
        The natural logarithm of x, for x> 0''')
    elif(function_name == 'max()'):
        print('''max(x1, x2,...)
        The largest of its arguments: the value closest to positive infinity''')
    elif(function_name == 'min()'):
        print('''min(x1, x2,...)
        The smallest of its arguments: the value closest to negative infinity''')