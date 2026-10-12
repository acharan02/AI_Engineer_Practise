#Electricity Bill Calculator
user = input("Enter your name: ")
units = float(input("Enter the number of units consumed: "))
if units < 0:
    print("Invalid input. Please enter a positive number of units.")
elif units <= 100:
    bill = units * 2
elif units <= 200:
    bill = 200 + (units - 100) * 3
else:
    bill = 500 + (units - 200) * 5
if units >= 0:
    print("Hello", user, "your electricity bill is:", bill)
