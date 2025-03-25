len("Hello")

# Exercise for knowing your data type.
print(type("Hello"))
print(type(12345))
print(type(123.45))
print(type(True))

# Type conversion quiz
print("Number of letters in your name: " + len(input("Enter your name: ")))

# My Solution
# Getting the length will yield integer. Thus, we need to convert it into string
print("Number of letters in your name: " + str(len(input("Enter your name: "))))

#Angela Yu solution
#Getting data type first
name_of_the_user = input("Enter your name: ")
length_of_name = len(name_of_the_user)

print(type("Number of letters in your name: "))
print(type(length_of_name))
#Converting the data type of int to string.
print("Number of letters in your name: " + str(length_of_name))