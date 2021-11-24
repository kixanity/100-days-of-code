# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
both = name1 + name2

t = (both.lower()).count('t')
r = (both.lower()).count('r')
u = (both.lower()).count('u')
e = (both.lower()).count('e')
true = t + r + u + e
print(f"Total = {true}")
l = (both.lower()).count('l')
o = (both.lower()).count('o')
v = (both.lower()).count('v')
e = (both.lower()).count('e')
love = l + o + v + e
print(f"Total = {love}")
love_score = str(true) + str(love)
if int(love_score) < 10 or int(love_score) > 90:
    print(f"Your score is {love_score}, you go together like Coke and Mentos.")
elif 50 > int(love_score) > 40:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")
