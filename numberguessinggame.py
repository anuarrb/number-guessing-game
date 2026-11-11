import random

attempts = 7

def display_rules():
    print("Welcome to the Number Guessing Game!\n")
    print("I have selected a random number between 1 and 100.")
    print(f"You have {attempts} attempts to guess the number.\n")

def check_guess(x, y):
    if x == y:
        return "correct"
    elif x < y:
        return "low"
    else:
        return "high"

def play_game(number, attempt=1):
    if attempt > attempts:
        print("\nGame Over!")
        print(f"The correct number was: {number}")
        return

    guess = input(f"Attempt {attempt}/{attempts} - Enter your guess (1-100): ")

    try:
        guess = int(guess)
    except ValueError:
        print("Please enter a valid number.\n")
        return play_game(number, attempt)

    if guess < 1 or guess > 100:
        print("Please enter a number between 1 and 100.\n")
        return play_game(number, attempt)
            
    result = check_guess(guess, number)

    if result == "correct":
        print(f"Congratulations! You've guessed the correct number: {number}")
        print(f"You guessed it in {attempt} attempts.")
        return
    elif result == "low":
        print("Your guess is too low. Try a higher number.\n")
    else:
        print("Your guess is too high. Try a lower number.\n")

    play_game(number, attempt + 1)

display_rules()

random_number = random.randint(1, 100)

play_game(random_number)