name = input("Apna naam likho: ")

with open("student.txt", "w") as file:
   
     file.write(name + "\n")

print("Data save ho gaya.")
