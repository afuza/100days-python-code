# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
height_total = height ** 2
bmi = weight / height_total

result_bmi = round(bmi)

print(result_bmi)