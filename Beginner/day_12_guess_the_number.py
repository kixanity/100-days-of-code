import random
# Number Guessing Game Objectives:
x = random.randint(1, 100)
print(x)
# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.

# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
life = 10
game_done = False
while not game_done:
    guess = int(input("Guess the number? "))
    if guess == x:
        print("That's correct!")
        game_done = True
    else:
        life -= 1
        if life == 0:
            print("No more life left.")
            game_done = True
        else:
            if guess < x:
                print("Try higher!")
                print(f"Lives left: {life}")
            else:
                print("Try lower!")
                print(f"Lives left: {life}")

# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

