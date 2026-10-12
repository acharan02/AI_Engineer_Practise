# exercise 2 with conditional statements
Name = input("What is your name? ")
Marks=int(input("Enter your marks: "))
if Marks >= 90:
    print("Hello", Name, "you have scored an A grade.")
elif Marks >= 80:
    print("Hello", Name, "you have scored a B grade.")
elif Marks >= 70:
    print("Hello", Name, "you have scored a C grade.")  
elif Marks >= 60:
    print("Hello", Name, "you have scored a D grade.")  
else :
    print("Hello", Name, "you have scored an F grade.")