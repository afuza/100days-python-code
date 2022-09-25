# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

my_name_lower = name1.lower()
curh_name_lower = name2.lower()

extend_name = my_name_lower + curh_name_lower

t = extend_name.count('t')
r = extend_name.count('r')
u = extend_name.count('u')
e = extend_name.count('e')

true_case = t + r + u + e

l = extend_name.count('l')
o = extend_name.count('o')
v = extend_name.count('v')
e = extend_name.count('e')

love_case = l + o + v + e

extend_true = str(true_case) + str(love_case)

result = int(extend_true)


if result <= 10 or result >= 90:
    print(f"Your score is {result}, you go together like coke and mentos.")
elif result >= 40 and result <= 50:
    print(f"Your score is {result}, you are alright together.")
else:
    print(f"Your score is {result}.")
