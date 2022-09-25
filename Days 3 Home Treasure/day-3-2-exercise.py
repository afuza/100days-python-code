# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
height_total = height ** 2
bmi = weight / height_total

result_bmi = round(bmi)

if result_bmi  <= 18.5:
    print(f"Your BMI is {result_bmi }, you are underweight.")
elif result_bmi  <= 25:
    print(f"Your BMI is {result_bmi }, you have a normal weight.")
elif result_bmi  <= 30:
    print(f"Your BMI is {result_bmi }, you are slightly overweight.")
elif result_bmi  <= 35:
    print(f"Your BMI is {result_bmi }, you are obese.")
else:
    print(f"Your BMI is {result_bmi }, you are clinically obese.")
