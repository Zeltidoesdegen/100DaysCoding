# Odd or even checker
number_input = int(input("Input number to check: "))
value_compute = number_input % 2

if value_compute == 0:
    print("Number is even")
else:
    print("Number is odd")

# Needs possible refactoring as compared to Angela Yu

# Angela Yu solution
number_to_check = int(input("What is the number you want to check? "))

if number_to_check % 2 == 0:
    print("Even")
else:
    print("Odd")