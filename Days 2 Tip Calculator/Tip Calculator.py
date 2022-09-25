print("Welcome to the tip calculator.")
bill = input("What was the total bill? $")
percentage = input("What percentage tip would yout like to give? 10, 12 or 15? ")
split_bill = input("How many people to split  the bill? ")


total_bill = float(bill)

point_percentage = int(percentage) / 100
point_bill = total_bill * point_percentage

toal_bill_tip = total_bill + point_bill

point_split = toal_bill_tip / int(split_bill) 
result = "{:.2f}".format(point_split)

print(f"Each person should pay: ${result}")