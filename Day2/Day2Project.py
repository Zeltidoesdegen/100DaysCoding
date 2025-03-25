# My solution
print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
tip_percentage = int(input("How much tip would you like to give? 10, 12, or 15? "))
split_bill_num = float(input("How many people to split the bill? "))

tip_value = (tip_percentage/100) * total_bill
final_value = total_bill + tip_value
shared_value = (final_value/split_bill_num)

print(f"Each person should pay: ${shared_value:.2f}")

# Angela Yu solution
# print("Welcome to the tip calculator!")
# total_bill = float(input("What was the total bill? $"))
# tip_percentage = int(input("How much tip would you like to give? 10, 12, or 15? "))
# split_bill_num = float(input("How many people to split the bill? "))
#
# tip_value = (tip_percentage/100) * total_bill
# final_value = total_bill + tip_value
# shared_value = (final_value/split_bill_num)
# final_amount = round(shared_value, 2)
#
# print(f"Each person should pay: ${final_amount}")