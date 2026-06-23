import random

print("Welcome to the game of Rock, Paper, Scissors!")

# Possible choices for the computer
choices = ["rock", "paper", "scissors"]

while True:
    # ask user their choice 
    user = input("Enter rock, paper or scissors: ").lower().strip()

    # Computer randomly selects a choice
    computer = random.choice(choices)

    print("Computer chose:", computer)

    # Tie case
    if user == computer:
        print("It's a tie!")

    # User winning cases
    elif user == "rock" and computer == "scissors":
        print("You win!")
    elif user == "scissors" and computer == "paper":
        print("You win!")
    elif user == "paper" and computer == "rock":
        print("You win!")

    # Computer winning cases
    elif computer == "rock" and user == "scissors":
        print("Computer wins!")
    elif computer == "scissors" and user == "paper":
        print("Computer wins!")
    elif computer == "paper" and user == "rock":
        print("Computer wins!")

    # Invalid input
    else:
        print("Invalid input!.")

    #play again logic
    play_again = input("Do you want to play again? (yes/no): ").lower().strip()

    if play_again != "yes":
        print("Thanks for playing!")
        break