name = input("Naam likho: ")

with open("student.txt", "a") as file:
    
     file.write(name + "\n")

print("Naam add ho gaya.")
