print("Welcome to the tip calculator!\n")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
split = int(input("How many people to split the bill? "))

total = bill +  bill * tip / 100
# split_bill = round(total / split, 2)
split_bill = total / split
final_amount = "{:.2f}".format(split_bill) # use format method instead of round() to always return 2 decimal places

print(f"Each person should pay: ${split_bill}")