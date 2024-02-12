print("WELCOME TO HANGMAN!") 

import random 

class Hangman: 
    def __init__(self, word_bank, difficulty):
        self.word_bank = word_bank
        self.difficulty = difficulty
        self.secret_word = self.secret_word()
        self.guesses_left = 6 
        self.guessed_letters = set()
        self.display_word = ['_'] * len(self.secret_word)

    def select_word(self):


    
    def display(self):



    def make_guess(self, letter):

