# Python script to generate and print a dictionary that contains a
# number (between 1 and n) in the form (x, x*x).

try:
    increment = 1
    get_number = int(input('Enter a number -> '))
    dicts = {}
    while get_number > 0:
        dicts[increment] = increment * increment
        get_number -= 1
        increment += 1
    print(dicts)
except ValueError as e:
    print(e)
