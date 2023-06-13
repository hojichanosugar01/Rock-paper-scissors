import random

# Function to determine the winner
def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (
        (player_choice == 'rock' and computer_choice == 'scissors') or
        (player_choice == 'paper' and computer_choice == 'rock') or
        (player_choice == 'scissors' and computer_choice == 'paper')
    ):
        return "You win!"
    else:
        return "You lose!"

# Main game loop
def play_game():
    choices = ['rock', 'paper', 'scissors']
    player_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    computer_choice = random.choice(choices)

    if player_choice in choices:
        print(f"Player: {player_choice}")
        print(f"Computer: {computer_choice}")
        print(determine_winner(player_choice, computer_choice))
    else:
        print("Invalid choice. Please enter either rock, paper, or scissors.")

# Start the game
play_game()
