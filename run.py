# Welcome message 
print("WELCOME TO HANGMAN!")

# Importing the random class
import random 

# Functions and classes 
class Hangman: 
    def __init__(self, word_bank, difficulty):
        self.word_bank = word_bank
        self.difficulty = difficulty
        self.secret_word = self.secret_word()
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

    def make_guess(self, letter):
         """
    This is the function for guessing a letter
        """
         
    def is_game_over(self):
         """
         This is the function which determines whether the game is over
         by running out of guesses or getting the word right
        """
    
    def play(self):
         """
         Function for playing the game
         """

# This is my current word bank, I might reduce the amount of words at a later stage
if __name__ == "__main__":
    word_bank = {
         "beginner": ["flow", "tuple", "output", "data", "set", "program"],
         "novice": ["command", "function", "variable", "iteration", "python", "javascript"],
         "professional": ["debugging", "structures", "oriented", "portfolio", "comparators", "exception" ]
         }
    
# These are my diffculties, which also will be changed in due course
    difficulty_level = input("Choose difficulty (beginner, novice, professional): ").lower()
    if difficulty_level not in word_bank:
         print("Invalid choice. The default difficulty is beginner")
         difficulty_level = "beginner"