#Angela Vasquez
#Extra Credit Lab CTC389

#Ask a user to guess what number you chose and give them the option to play.

def GuessingGame():

    x = 0

    while (x != 7):
        x = float(input("Guess my number! Enter a number, any number between 1 and 20: "))
   
    if (x == 7):
        print("You won! You must be a psychic! " ,x)

    elif (x <= 10)and (x >= 4):
        print("You are incorrect, please guess again")
   
    elif (x < 5):
        print("I'm sorry, but you lost. My number was higher.")

    elif(x > 9):
        print("I'm sorry, but you lost. My number was lower.")

play = input("Would you like to play the guessing game? ")

while (play == "yes"):
    GuessingGame()
    play = input("Would you like to play again? ")

print("Thanks for playing!")
