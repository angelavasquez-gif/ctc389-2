#Angela Vasquez
# CTC389 Lab 1a

#Ask a user to guess what number you chose.

x = 34

while (x != 33):
    x = float(input("Guess my number! Enter a number, any number between 1 and 50: "))
    if (x != 33):
        print("You are incorrect, please guess again")
    if (x == 33):
        print("You won! You must be a psychic! " ,x)


