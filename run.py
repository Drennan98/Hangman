# Import art 
from art import *

# Welcome message 
print(text2art("Hangman!", space=1))

# Importing the random class
import random 

# Functions and classes 
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
        print(f"Guessed letters: {self.guessed_letters}")

    def make_guess(self, letter):
        """
        This is the function for guessing a letter
        :param letter: guessed letter
        """
        if letter in self.guessed_letters: 
            print("You have already guessed that letter. Please pick a different letter")
            return
        
        self.guessed_letters.add(letter)

        if letter in self.secret_word:
            for x in range(len(self.secret_word)):
                if self.secret_word[x] == letter:
                    self.display_word[x] = letter

        else:
            self.guesses_left -= 1

    def is_game_over(self):
        """
         This is the function which determines whether the game is over
         by running out of guesses or getting the word right
        """
        if "_" not in self.display_word:
            print("Well done! You guessed the correct word, which was:", self.secret_word)
            return True
        elif self.guesses_left == 0:
            print("The game is over! The word was:", self.secret_word)
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
                print("Please enter a single letter.")

# This is my current word bank, I might reduce the amount of words at a later stage
if __name__ == "__main__":
    word_bank = {
         "beginner": ["flow", "tuple", "output", "data", "set", "program"],
         "novice": ["command", "function", "variable", "iteration", "python", "javascript"],
         "professional": ["debugging", "structures", "oriented", "portfolio", "comparators", "exception" ]
         }
    
# I came across an issue where the game would end when I picked a difficulty that
# wasn't available. So I used a While Loop, the commit message for this change is rather long
# so I'm putting in a comment to explain what I was thinking. 
while True:
    difficulty_level = input("Choose difficulty (beginner, novice, professional): ").lower()
    if difficulty_level not in word_bank:
         print("Invalid choice. Please select from one of the available difficulties")  
    else:
        hangman_game = Hangman(word_bank, difficulty_level)
        hangman_game.play()
        break