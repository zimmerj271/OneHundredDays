from random import randint
from art import logo

# Global constants
EASY_NUMBER_TURNS = 10
HARD_NUMBER_TURNS = 5
NUMBER_RANGE = 100

def get_difficulty():
    difficulty = input("Choose a diffiuclty. Type 'easy' or 'hard': ")
    if difficulty == 'easy':
        number_tries = EASY_NUMBER_TURNS
    else:
        number_tries = HARD_NUMBER_TURNS
    return number_tries

def check_answer(guess_number, correct_number):
    if guess_number > correct_number:
        print("Too high, guess again.")
    elif guess_number < correct_number:
        print("Too low, guess again")
    elif guess_number == correct_number:
        return True
    else:
        print("Please guess a number between 1 and 100.")
    return False

def play_round(try_count, correct_number):
    while try_count > 0:
        print(f"You have {try_count} attempts remaining to guess the number.")
        player_guess = int(input("Make a guess: "))
        if check_answer(player_guess, correct_number):
            return True
        else:
            try_count -= 1
    return False

def guessing_game():

    number = randint(1, NUMBER_RANGE)
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between 1 and {NUMBER_RANGE}.")
    print(f"Psssst, the correct answer is {number}")

    num_tries = get_difficulty()
    win = play_round(num_tries, number)
    if win:
        print(f"You got it! The answer is {number}.")
    else:
        print("You've run out of guesses, you lose.")

guessing_game()
