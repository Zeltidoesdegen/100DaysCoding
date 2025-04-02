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


while choice1 not in ("LEFT", "RIGHT"):
    choice1 = str.upper(input("Where do you want to go? Left or Right? "))
    if choice1 == "LEFT":
        print("You've come to a lake. There is an island in the middle of the lake.")
    elif choice1 == "RIGHT":
        print("You fell into a hole. Game Over.")
        exit()
    else:
        print("You've input a wrong answer, please choose again.")

choice2 = ""

while choice2 not in ("SWIM", "WAIT"):
    choice2 = str.upper(input("Swim or Wait? "))
    if choice2 == "WAIT":
        print("You arrive at the island unharmed. There is a house with 3 doors.")
    elif choice2 == "SWIM":
        print("You get attacked by an angry trout. Game Over.")
    else:
        print("You've input a wrong answer, please choose again.")

choice3 = ""

while choice3 not in ("Red", "Blue", "Yellow"):
    choice3 = str.upper(input("Which door? Yellow, Blue, Red? "))
    if choice3 == "YELLOW":
        print("You Win! You found the treasure")
    elif choice3 == "BLUE":
        print("Eaten by bests. Game Over!")
    elif choice3 == "RED":
        print("It's a room full of fire. Game Over.")
    else:
        print("You've input a wrong answer, please choose again.")

# Notes to self
# Refactoring needs to be made. Nested if else is the more cleaner way.