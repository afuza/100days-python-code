# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# if year % 4 == 0:
#     print("Leap year.")
# elif year % 100 == 0:
#     print("Leap year.")
# elif year % 400 == 0:
#     print("Leap year.")
# else:
#     print("Not leap year.")



leap_tuch = year % 4
not_leap = year % 100
leap_i = year % 400

if leap_tuch == 0:
    if not_leap == 0:
        if leap_i == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")
