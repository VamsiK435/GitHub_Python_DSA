username = input("Enter username: ")
password = input("Enter the password: ")

if username == "admin" and password == "admin":
    print("You can reset")
else:
    print("You cannot reset")
