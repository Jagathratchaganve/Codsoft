import random

def rock_paper_scissors():
    """A simple rock-paper-scissors game."""

    # Define the possible choices
    choices = ["rock", "paper", "scissors"]

    # Keep track of scores
    user_score = 0
    computer_score = 0

    while True:
        # Get user input
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()

        # Validate user input
        if user_choice not in choices:
            print("Invalid choice. Please enter rock, paper, or scissors.")
            continue

        # Generate computer's choice
        computer_choice = random.choice(choices)

        # Determine the winner
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("You win!")
            user_score += 1
        else:
            print("You lose!")
            computer_score += 1

        # Display scores
        print("Your score:", user_score)
        print("Computer score:", computer_score)

        # Ask to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

if __name__ == "__main__":
    rock_paper_scissors()