# exercise 3 with conditional statements
username = input("What is your name? ")
Password = input("Enter your password: ")
admin_username = "Sonic"
admin_password = "12345"
if username == admin_username:
    if Password == admin_password:
         print("Hello", username, "you have successfully logged in.")
    else:
        print("Hello", username, "you have entered an invalid password.")
else:
    print("Hello", username, "you have entered an invalid username.")
