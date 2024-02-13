# Welcome message 
print("WELCOME TO HANGMAN!") 

# Importing the random class
import random 

class Hangman: 
    def __init__(self, word_bank, difficulty):
        self.word_bank = word_bank
        self.difficulty = difficulty
        self.secret_word = self.secret_word()
        self.guesses_left = 6 
        self.guessed_letters = set()
        self.display_word = ['_'] * len(self.secret_word)

    """
    This function is used to select a word at random
    """
    def select_word(self):


    """
    This functions is for displaying the game
    """
    def display(self):


    """
    This is the function for guessing a letter
    """
    def make_guess(self, letter):

