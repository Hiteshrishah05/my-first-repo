import random

print("welcome to the game of dice roller")

while True:
    #ask user if they want to roll the dice or not
    choice = input("roll the dice? (yes or no):")
    if choice=="yes" :
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        print(f"you rolled a {die1} and {die2}!")
    elif choice=="no":
        print("thenks for playing!")
        break
    else:
        print("invalid input. please select yes or no")