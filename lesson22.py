password = input("Password likho: ")

if len(password) < 8:
    print("Weak Password")
elif len(password) < 12:
    print("Medium Password")
else:
    print("Strong Password")
