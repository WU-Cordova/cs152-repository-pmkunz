import copy
import random
from projects.project1.card import Suit, Face, Card
from datastructures.bag import Bag

class MultiDeck:

    def __init__(self, num_decks: int = 1):
        """ Initializes the deck, using a specific number of decks """
        one_deck_list = [Card(face, suit) for suit in Suit for face in Face]
        self.deck_count = num_decks
        self.num_cards = 52 * self.deck_count
        self.multi_deck_list = [card for _ in range(self.deck_count) for card in copy.deepcopy(one_deck_list)]
        self.deck_bag = Bag(*self.multi_deck_list)
        
    def deal_card(self):
        """ Deals a card from the deck """
        
        deck_list = list(self.deck_bag.distinct_items())                            # distinct_items() from bag.py
        deck_list = [card for card in deck_list if self.deck_bag.count(card) > 0]   # Get rid of cards that have a count of 0

        # Check that none of the keys have values of 0
        for card in deck_list:
            if self.deck_bag.count(card) == 0:
                deck_list.remove(card)

        #if there are no cards left in the deck:
        if len(deck_list) == 0:
            raise ValueError("The deck is empty.")

        card = random.choice(deck_list)
        self.deck_bag.remove(card)
        self.num_cards -= 1                                     # Subtract 1 card from the counter
        return card

    def get_deck_size(self):
        """ Returns the number of cards left in the deck """
        return self.num_cards