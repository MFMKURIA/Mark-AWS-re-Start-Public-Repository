import random


def guess_number_game():
    """
    This function starts a game where the user has to guess a random number between 1 and 100.
    The function will keep asking the user for guesses until they correctly guess the number.
    It will also keep track of the number of attempts it takes for the user to guess the correct number.

    Parameters:
    None

    Returns:
    None
    """

    # Print welcome message and instructions
    print("Welcome to the Random Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100. Try to guess it!")

    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0

    # Start the game loop
    while True:
        try:
            # Ask the user for their guess
            guess = int(input("Enter your guess (between 1 and 100): "))
            attempts += 1

            # Check if the guess is within the valid range
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue

            # Check if the guess is too low, too high, or correct
            if guess < secret_number:
                print("Too low! Try a higher number.")
            elif guess > secret_number:
                print("Too high! Try a lower number.")
            else:
                # Congratulate the user and display the number of attempts it took them to guess correctly
                print(
                    f"Congratulations! You guessed the number {secret_number} in {attempts} attempts!"
                )
                break

        except ValueError:
            # Handle invalid input by displaying an error message
            print("Invalid input. Please enter a valid number.")


# This line of code is a function call to start the "guess the number" game. The function is not provided in the code snippet you provided, but it is likely a custom function that starts a game where the user has to guess a random number between 1 and 100.
if __name__ == "__main__":
    guess_number_game()
