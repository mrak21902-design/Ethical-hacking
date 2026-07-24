import random
import string

length = int(input("Password ki length: "))

chars = string.ascii_letters + string.digits + string.punctuation

password = ""

for i in range(length):
    password += random.choice(chars)

print("Generated Password:", password)
