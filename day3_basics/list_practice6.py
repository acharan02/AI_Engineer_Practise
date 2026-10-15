numbers = [1, 2, 3, 2, 4, 1, 5, 3, 6]
duplicate = []
for number in numbers:
    if numbers.count(number) > 1 and number not in duplicate:
        duplicate.append(number)
print(duplicate)