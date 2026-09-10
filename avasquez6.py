#Angela Vasquez
#Lab 6 CTC389
#List of Students & Index

students = ["Punky Brewster", "Belvedere", "Alf", "Fonzie", "Alex P. Keaton"]

print("Current Student List")
for i in students:
    print(i)

print("Menu")
print("------------------")
print("Option 1: Add a student to the list.")
print("Option 2: Modify a student name.")
print("Option 3: Remove a student.")

option = int(input("What option would you like to choose?"))

if(option == 1):
    name = input("Enter the name of a student you would like to add to the list.")
    students.append(name)
    for i in students:
        print(i)

if(option == 2):
    c = 0
    for i in students:
        c = c + 1
        print(c,i)
    x = int(input("Which student do you want to change? "))
    name = input("Enter name to change to: ")
    students[x-1] = name
    for i in students:
        print(i)

if(option == 3):
    c = 0
    for i in students:
        c = c + 1
        print(c,i)
    x = int(input("Which student do you want to remove? "))
    students.pop(x-1)
    for i in students:
        print(i)
