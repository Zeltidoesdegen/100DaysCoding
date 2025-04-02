print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
bill = 0

if size == "S":
    bill = 15
    if pepperoni == "Y":
        bill += 2
    elif pepperoni == "N":
        bill += 0
    else:
        print("That is not a correct input, we will not add value")

    if extra_cheese == "Y":
        bill += 1
    elif extra_cheese == "N":
        bill += 0
    else:
        print("That is not a correct input, we will not add value")
elif size == "M":
    bill = 20
    if pepperoni == "Y":
        bill += 3
    elif pepperoni == "N":
        bill += 0
    else:
        print("That is not a correct input, we will not add value")

    if extra_cheese == "Y":
        bill += 1
    elif extra_cheese == "N":
        bill += 0
    else:
        print("That is not a correct input, we will not add value")
elif size == "L":
    bill = 25
    if pepperoni == "Y":
        bill += 3
    elif pepperoni == "N":
        bill += 0
    else:
        print("That is not a correct input, we will not add value")


    if extra_cheese == "Y":
        bill += 1
    elif extra_cheese == "N":
        bill += 0
    else:
        print("That is not a correct input, we will not add value")
else:
    print("Please restart and put a correct size")


print(f"Your final bill is: ${bill}.")

# Learnings:
# The "If" statement should be within the cluster to commence, if not it won't.
# Each "If" statement should have its own nested condition.

# Angela Yu solution
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("You have chosen an invalid size.")


if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3


if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")

# Lesson learned
# You can still commence the code outside the if statement and continue.
# Refactoring still needs a bit of practice to get cleaner and reusable code.