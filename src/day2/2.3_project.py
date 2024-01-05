print('''
888                                                         d8b        888 
888                                                         Y8P        888 
888                                                                    888 
888888888d888 .d88b.  8888b. .d8888b 888  888888d888 .d88b. 888.d8888b 888 
888   888P"  d8P  Y8b    "88b88K     888  888888P"  d8P  Y8b88888K     888 
888   888    88888888.d888888"Y8888b.888  888888    88888888888"Y8888b.888 
Y88b. 888    Y8b.    888  888     X88Y88b 888888    Y8b.    888     X88888 
 "Y888888     "Y8888 "Y888888 88888P' "Y88888888     "Y8888 888 88888P'888 
 ''')

print("Welcome to the treasure island.")
print("Your mission is to find the treasure.")
choice1 = input("you are at a crossroad, where do you want to go 'Left' or 'right'.").lower()
if choice1 == "left":
    choice2 = input("you've come to a lake. There is an island in the middle of the lake. Type 'Wait' to wait for a boat. Type 'swim' to swim across.").lower()
    if choice2 == "wait":
        # game will continue
        choice3 = input("you arrive at the island unharmed. There is a house with three doors. one red one yellow and one blue. Which color do you choose?").lower()
        if choice3 == "red":
            print("it's a room full of fire. Game over.")
        elif choice3 == "yellow":
            print("you find the Treasure! You win!")
        elif choice3 == "blue":
            print("you enter a room of beasts. Game over.")
        else:
            print("you chose a door that doesn't exist. Game Over.")
    else:
        print("you got attacked by an angry trout. Game over.")
else:
    print("You fell into a hole. Game over")