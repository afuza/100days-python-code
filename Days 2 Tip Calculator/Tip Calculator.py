#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator.")
bill = input("What was the total bill? $")
percentage = input("What percentage tip would yout like to give? 10, 12 or 15? ")
split_bill = input("How many people to split  the bill? ")


total_bill = float(bill)

point_percentage = int(percentage) / 100
point_bill = total_bill * point_percentage

toal_bill_tip = total_bill + point_bill

point_split = toal_bill_tip / int(split_bill) 


print(f"Each person should pay: ${round(point_split,2)}")