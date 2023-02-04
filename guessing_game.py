"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------
"""

import random
import sys

name = input("What is your name?  ")

print(f"Welcome to the number guessing game {name}! 😄")


def get_guess(attempts, answer):
    try:
        guess = int(
            input("Try to guess the random number between 1 and 10.  "))
        if guess > 10 or guess < 1:
            # Handle out of range guesses
            print(
                f"{guess} is out of range 😕 the random number is between 1 and 10")
            attempts += 1
            get_guess(attempts, answer)
        elif guess > answer:
            print("It's lower ⬇")
            attempts += 1
            get_guess(attempts, answer)
        elif guess < answer:
            print("It's higher ⬆")
            attempts += 1
            get_guess(attempts, answer)
        else:
            # Correct guess
            # TODO: save and update high_score
            print(
                f"Got it! 🥳 \n It took {attempts} attempts to get the correct number \n Game over 👋. \n Thank you for playing {name} 😄")
    except ValueError as err:
        # Handle invalid value guesses
        print("Oh no! That's not a valid number 😕. Try again...")
        print(f"({err})")
        attempts += 1
        get_guess(attempts, answer)
    else:
        return guess


def start_game():
    # TODO: Display the current high_score
    # Reset attempts and new random number before each round
    attempts = 0
    answer = random.randint(1, 10)
    get_guess(attempts, answer)
    # Prompt player if they would like to replay
    replay_choice = (input("Would you like to play again? Y/N?  ")).lower()
    while replay_choice != "y" and replay_choice != "n":
        # Handle invalid input
        print('Oops 😕 ... please enter either "Y" or "N"')
        replay_choice = (input("Would you like to play again? Y/N?  ")).lower()
    if replay_choice == "n":
        sys.exit(
            f"Thank you for playing the random number guessing game {name} 😸")
    while replay_choice == "y":
        start_game()


start_game()
