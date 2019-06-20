numbers = [1, 6, 2, 10, 3, 8, 7, 5]
max_number = min_number = numbers[0]

for num in numbers:
    if num > max_number:
        max_number = num

    if num < min_number:
        min_number = num

print("maximum : ", max_number)
print("minimum : ", min_number)
