import copy
import random
from datastructures.bag import Bag
from projects.project1.card import Card, Suit, Face
from projects.project1.game import Game

# before running, enter this into the terminal:
# export PYTHONPATH=/Users/pkmckenna/Documents/GitHub/cs152-repository-pmkunz:$PYTHONPATH

def main():

    print("Welcome to Blackjack!")

    game = Game()
    game.start_game()

if __name__ == '__main__':
    main()
    
