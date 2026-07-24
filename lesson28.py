correct_username = "admin"
correct_password = "12345"

for i in range(3):
    username = input("Username: ")
    password = input("Password: ")

    if username == correct_username and password == correct_password:
        print("Login Successful")
        break
    else:
        print("Wrong Username or Password")

else:
    print("Account Locked")
