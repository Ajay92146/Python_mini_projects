import random  # Used to generate the computer's random choice

# -----------------------------
# Take input from the player
# -----------------------------
# The input is converted to lowercase to ensure case-insensitive comparison
player = input("Enter your choice [rock, paper, scissor]: ").lower()

# -----------------------------
# Define valid choices
# -----------------------------
# List of all possible options in the game
choices = ['rock', 'paper', 'scissor']

# Randomly select one choice for the computer
computer = random.choice(choices)

# -----------------------------
# Game logic and result
# -----------------------------
# If both player and computer choose the same option, the game is a tie
if player == computer:
    print(f"Tie! You chose {player} and the computer chose {computer}.")

# Player chooses rock
elif player == "rock":
    if computer == "scissor":
        print(f"You win! You chose {player} and the computer chose {computer}.")
    else:
        print(f"You lose! You chose {player} and the computer chose {computer}.")

# Player chooses paper
elif player == "paper":
    if computer == "rock":
        print(f"You win! You chose {player} and the computer chose {computer}.")
    else:
        print(f"You lose! You chose {player} and the computer chose {computer}.")

# Player chooses scissor
elif player == "scissor":
    if computer == "paper":
        print(f"You win! You chose {player} and the computer chose {computer}.")
    else:
        print(f"You lose! You chose {player} and the computer chose {computer}.")

# Handles invalid input from the user
else:
    print("Invalid choice! Please enter rock, paper, or scissor.")
