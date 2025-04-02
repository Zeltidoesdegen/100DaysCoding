print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height > 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill += 5
        print("Please pay $5.")
    elif age <= 18:
        bill += 7
        print("Please pay $7.")
    elif age >= 45 and age <= 55:
        print("Your ride is free.")
    else:
        bill += 12
        print("Please pay $12.")

    wants_photo = input("Do you want a photo take? Y or N. ")
    if wants_photo == "Y":
        bill += 3
else:
    print("Sorry you have to grow taller before you can ride.")

print(f"Your total bill is ${bill}.")