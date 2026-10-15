numbers = [23, 67, 12, 89, 45, 34]
largest = numbers[0]
for i in numbers:
    if i > largest:
        largest = i
print("Largest element:", largest)