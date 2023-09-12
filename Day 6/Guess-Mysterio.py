import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

# Initialize variables
attempts = 0
is_guess_correct = False

print("Welcome to the Guess the Number game!")
print("I'm thinking of a number between 1 and 100. Can you guess it?")

# Main game loop
while not is_guess_correct:
    try:
        # Get user's guess
        user_guess = int(input("Enter your guess: "))
        attempts += 1

        # Check if the guess is correct
        if user_guess == secret_number:
            is_guess_correct = True
        elif user_guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Game over
print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
