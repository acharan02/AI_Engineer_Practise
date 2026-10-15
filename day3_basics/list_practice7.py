numbers = [45, 12, 89, 33, 7, 56]
print(sorted(numbers))
print(sorted(numbers, reverse=True))

names = ["Charan", "Rahul", "Priya", "Sneha"]
print(list(reversed(names)))

original = [10, 20, 30, 40]
new_list = original.copy()
new_list.append(50)
print(original)
print(new_list)