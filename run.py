# Import art and color

from art import *
from termcolor import colored

# Import random

import random

# Welcome message

print(text2art("Hangman!", space=0))
print(text2art("Best Of Luck :D"))

# Functions and classes


def display_hangman(guessed_letters):
    stages = [
     """
    --------
    |      |
    |
    |
    |
    |
    |
    """,
     """
    --------
    |      |
    |      O
    |
    |
    |
    |
    """,
     """
    --------
    |      |
    |      O
    |      |
    |
    |
    |
    """,
     """
    --------
    |      |
    |      O
    |     /|
    |
    |
    |
    """,
     """
    --------
    |      |
    |      O
    |     /|\\
    |
    |
    |
    """,
     """
    --------
    |      |
    |      O
    |     /|\\
    |     / \\
    |
    |
    """
    ]
    print(stages[guessed_letters])


class Hangman:
    def __init__(self, word_bank, difficulty):
        self.word_bank = word_bank
        self.difficulty = difficulty
        self.secret_word = self.select_word()
        self.guesses_left = 6
        self.guessed_letters = set()
        self.display_word = ['_'] * len(self.secret_word)

    def select_word(self):
        """
        This function is used to select a word at random
        """
        return random.choice(self.word_bank[self.difficulty])

    def display(self):
        """
        This functions is for displaying the game
        """
        print(" ".join(self.display_word))
        print(f"Number of guesses left: {self.guesses_left}")
        print(f"Guessed letters: {', '.join((self.guessed_letters))}")

    def make_guess(self, letter):
        """
        This is the function for guessing a letter
        :param letter: guessed letter
        """
        if letter in self.guessed_letters:
            print(colored("You already guessed that letter! "
                  "Please pick a different letter!", "yellow"))
            return
        self.guessed_letters.add(letter)

        if letter in self.secret_word:
            for x in range(len(self.secret_word)):
                if self.secret_word[x] == letter:
                    self.display_word[x] = letter

        else:
            self.guesses_left -= 1
            guesses_used = (5 - self.guesses_left)
            display_hangman(guesses_used)

    def is_game_over(self):
        """
         This is the function which determines whether the game is over
         by running out of guesses or getting the word right
        """
        if "_" not in self.display_word:
            print(colored("You guessed the correct word!"), self.secret_word)
            return True
        elif self.guesses_left == 0:
            print(colored("The game is over! "
                  "The correct word was!", "blue"), self.secret_word)
            return True
        return False

    def play(self):
        """
        Function for playing the game
        """
        while not self.is_game_over():
            self.display()
            guess = input("Enter your guess: ").lower()

            if len(guess) == 1 and guess.isalpha():
                self.make_guess(guess)
            else:
                print(colored("Please enter a single letter!", "blue"))

# This is my current word bank


if __name__ == "__main__":
    word_bank = {
         "beginner": ["flow", "tuple", "output", "data", "set", "program"],
         "novice": ["command", "function", "variable", "iteration", "python"],
         "professional": ["debugging", "structures", "portfolio", "importing"]
         }

# While Loop for running the game

while True:
    difficulty_level = input("Choose from beginner, novice or professional: ")
    if difficulty_level not in word_bank:
        print(colored("Wrong choice. Please select from difficulties!", "red"))
    else:
        hangman_game = Hangman(word_bank, difficulty_level)
        hangman_game.play()
        break
