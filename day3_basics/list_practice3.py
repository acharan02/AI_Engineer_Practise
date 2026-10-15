fruits = ["apple", "banana", "cherry", "date", "elderberry"]
for i in fruits:  # Iterate over a copy of the list
    if len(i) % 2 == 0:
        fruits.remove(i)  
print(fruits)