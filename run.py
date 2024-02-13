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


    word_bank = {
         "beginner": ["flow", "tuple", "output", "data", "set", "program"],
         "novice": ["command", "function", "variable", "iteration", "python", "javascript"],
         "professional": ["debugging", "structures", "oriented", "portfolio", "comparators", "exception" ]
         }

    difficulty_level = input("Choose difficulty (easy, medium, hard): ")