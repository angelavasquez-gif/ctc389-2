#Angela Vasquez
#Lab 8 CTC389
#Chose Your Own Adventure

PlayAgain = "yes"

while PlayAgain == "yes":
    print("Welcome Traveler!")
    name = input("What is your name? ")

    print()
    print("Hello", name)
    print("You have entered the amazing Halloween Adventure Park!") 
    print("Please choose how you will travel through our park.") 
    print()

#Decision #1

    print("You walk up to the attendant to decide which path you will take first.")
    print("Option 1: Take a spin on the Zombie-a-Whirl.")
    print("Option 2: Walk through the Haunted House!")
    print("Option 3: Travel through Frankenstein's Maze.")
    option = input("What option would you like to choose? ")

    if(option == 1):
        print("You get on the Zombie-a-Whirl and an actual zombie lurches at you.")
    elif(option == 2):
        print("You walk into the haunted house, and a ghost chases you out again.")
    elif(option == 3):
        print("You walk into the maze, turn a corner, and Frankenstein looms over you.")

    print()

#Decision #2

    print("You run down the path towards a building with its lights on. Where will you go?")
    print("Option 1: Run through the front door.")
    print("Option 2: Run around the back and behind the building.")
    print("Option 3: Climb the ladder up to the second floor, and climb through the window.")
    option = input("What option would you like to choose? ")

    if(option == 1):
        print("You enter through the front door and fall through a trap door.")
    elif(option == 2):
        print("You run around the back of the house and fall into a trap.")
    elif(option == 3):
        print("You climb through the window and are locked inside a small room.")

    print()

#Decision #3

    print("You find yourself trapped. How will you escape?")
    print("Option 1: Yell out for help.")
    print("Option 2: Tap out a message in morse code.")
    print("Option 3: Feel around the room looking for a latch.")
    option = input("What option would you like to choose? ")

    if(option == 1):
        print("The door opens, and a small, green man stares at you from the other side.")
    elif(option == 2):
        print("The door opens, and a ghost in a military uniform stares at you.")
    elif(option == 3):
        print("The door opens, and you stare into the empty eyes of a shadowy figure.")

    print()

#Decision #4

    print("What will you say to the figure standing in front of you?")
    print("Option 1: Nothing, just walk past and hope for the best.")
    print("Option 2: Please help me, I want to go home.")
    print("Option 3: Get out of my way! You don't scare me!")
    choice = input("What option would you like to choose? ")

    if(option == 1):
        print("You attempt to walk past the figure, and it blocks your path.")
    elif(option == 2):
        print("You ask for help, but the figure just laughs and blocks your path.")
    elif(option == 3):
        print("The figure chooses not to move, and you are blocked still.")

    print()

#Decision #5

    print("The figure tells you that in order to escape, you must pass a test.")
    print("Option 1: You have to answer a riddle.")
    print("Option 2: You have to solve a math equation.")
    print("Option 3: You have to perform an interpretive dance.")
    choice = input("What option would you like to choose? ")

    if(option == 1):
        print("You successfully answer a riddle about a cow, and a door opens.")
        print(name, " you escaped the house and may walk to freedom!")
    elif(option == 2):
        print("You solve an algebraic equation, and a door opens.")
        print(name, " you escaped the house and may walk to freedom!")
    elif(option == 3):
        print("You perform and interpretive dance about broccoli, and a door opens.")
        print(name, " you escaped the house and may walk to freedom!")

    print()

    PlayAgain = input("Would you like to play again? ")

print()
print("Thanks for playing!")
