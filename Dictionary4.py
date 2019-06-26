# Python program to iterate over dictionaries using for loops.

dicts = {'FirstName': 'Sanket', 'lastName': 'Sontakke', 'age': 25, 'Location': 'Mumbai',
         'Address': {'City': 'Navi Mumbai', 'State': 'Maharashtra', 'PinCode': '400701'}}

for key, val in dicts.items():
    print(key, ' - ', val)

