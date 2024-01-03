# A program that plays rock-paper-scissors with the user
import random

# Define the choices and the rules
choices = ["rock", "paper", "scissors"]
rules = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}

# Ask the user for their choice
user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()

# Validate the user's choice
if user_choice not in choices:
    print("Invalid choice. Please try again.")
else:
    # Generate a random choice for the computer
    computer_choice = random.choice(choices)

    # Print the computer's choice
    print("The computer chose:", computer_choice)

    # Compare the choices and determine the winner
    if user_choice == computer_choice:
        print("It's a tie.")
    elif rules[user_choice] == computer_choice:
        print("You win!")
    else:
        print("You lose.")
