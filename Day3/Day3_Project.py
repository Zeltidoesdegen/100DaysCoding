print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = ""
choice2 = ""
choice3 = ""


while choice1 != ("LEFT", "RIGHT"):
    choice1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right"').upper()
    if choice1 == "LEFT":
        while choice2 != ("SWIM", "WAIT"):
            choice2 = input('You\'ve come to a lake. '
                        'There is an island in the middle of the lake. '
                        'Type "wait" to wait for a boat. '
                        'Type "swim" to swim across.\n').upper()
            if choice2 == "WAIT":
                while choice3 != ("Red", "Blue", "Yellow"):
                    choice3 = input("You arrive at the island unharmed. "
                                    "There is house with 3 doors. One red, "
                                    "one yellow and one blue. "
                                    "Which colour do you choose?\n").upper()
                    if choice3 == "YELLOW":
                        print("You Win! You found the treasure")
                        exit()
                    elif choice3 == "BLUE":
                        print("Eaten by bests. Game Over!")
                        exit()
                    elif choice3 == "RED":
                        print("It's a room full of fire. Game Over.")
                        exit()
                    else:
                        print("You've input a wrong answer, please choose again.")

            elif choice2 == "SWIM":
                print("You get attacked by an angry trout. Game Over.")
                exit()
            else:
                print("You've input a wrong answer, please choose again.")

    elif choice1 == "RIGHT":
        print("You fell into a hole. Game Over.")
        exit()
    else:
        print("You've input a wrong answer, please choose again.")

# Notes to self
# Refactor the breaks
# Addition of counters - possible if too many mistakes, make game over
# Refactor exit in future
# Make it a bit more lengthy.