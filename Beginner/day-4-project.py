rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇

import random
fist = [rock, paper, scissors]
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
human = fist[choice]
cpu = fist[random.randint(0, 2)]
print(human)
print(cpu)

if human == cpu:
    print("Draw.")
elif cpu == paper and not human == scissors:
    print("You Lose.")
elif cpu == rock and not human == paper:
    print("You Lose.")
elif cpu == scissors and not human == rock:
    print("You Lose.")
else:
    print("You Win.")
