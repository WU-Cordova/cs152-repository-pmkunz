import random
import copy
from datastructures.bag import Bag
from projects.project1.card import Card, Suit, Face
from projects.project1.multideck import MultiDeck


class Game:

    def __init__(self):
        """ Initializes the game """
        deck_count = random.choice([2, 4, 6, 8])
        self.deck = MultiDeck(deck_count)

    def calculate_hand_value(self, hand: list) -> int:
        """ Returns the total value of the hand """
        return sum(card.face.face_value() for card in hand if card is not None)
    
    def display_hand(self, hand: list, player: bool = True, reveal_dealer: bool = False) -> None:
        """ Displays the player's or dealer's hand and scores """
        hand_str = " ".join(str(card) for card in hand)
        score = self.calculate_hand_value(hand)
        if player:
            print(f"Player's hand: {hand_str} | score: {score}")
        else: #dealer
            if reveal_dealer: # dealer shows both cards
                print(f"Dealer's hand: {hand_str} | score: {score}")
            else: # dealer shows one card and hides the other
                print(f"Dealer's hand: {hand[0]} [hidden] | score: {hand[0].face.face_value()}")
 
    def start_game(self):
        """ Starts the Blackjack game """

        while True: # while loop allows for multiple fames to be played

            player_hand = []
            dealer_hand = []
            # Player and Dealer are each dealt two cards:
            for i in range(2):
                player_hand.append(self.deck.deal_card())
                dealer_hand.append(self.deck.deal_card())

            # Display initial deal
            print() # blank line
            print("Initial deal:")
            self.display_hand(player_hand)
            self.display_hand(dealer_hand, player=False)
            print() # blank line

            # Check if the player has Blackjack
            if self.calculate_hand_value(player_hand) == 21:
                print("Player has Blackjack! Player wins!")
                play_again = input("\nWould you like to play again? (Y)es or (N)o: ").strip().lower()
                if play_again != 'y' and play_again != 'yes':
                    print("Game over! Thanks for playing.")
                    break
                else:
                    continue

            # Player's turn:
            while self.calculate_hand_value(player_hand) < 21:
                self.display_hand(player_hand)
                action = input("Do you want to 'hit' or 'stay'?").strip().lower()
                print() # blank line
                if action == 'h' or action == 'hit':
                    player_hand.append(self.deck.deal_card())
                elif action == 's' or action == 'stay':
                    break
                else:
                    print("Invalid input. Choose 'H' to Hit or 'S' to Stay.")

            # Check to see if player busts
            if self.calculate_hand_value(player_hand) > 21:
                self.display_hand(player_hand)
                print("Bust! You went over 21.")
                print() # blank line
                print("Dealer's hand: ", " ".join(str(card) for card in dealer_hand))
                print("Dealer wins! Player busted.")
            else:
            # Dealer's turn:
                print("\nDealer's turn:")
                self.display_hand(dealer_hand, player=False, reveal_dealer = True)
                while self.calculate_hand_value(dealer_hand) < 17:
                    dealer_hand.append(self.deck.deal_card())
                    self.display_hand(dealer_hand, player=False, reveal_dealer = True)

                # Who won?
                player_score = self.calculate_hand_value(player_hand)
                dealer_score = self.calculate_hand_value(dealer_hand)
                if player_score > 21:
                    print("Player busts! Dealer wins.")
                elif dealer_score > 21:
                    print("Dealer busts! Player wins.")
                elif player_score > dealer_score:
                    print("Player wins!")
                elif dealer_score > player_score:
                    print("Dealer wins!")
                else:
                    print("It's a tie!")

            # Does the player want to play again?
            play_again = input("\nWould you like to play again? (Y)es or (N)o: ").strip().lower()
            if play_again != 'y' and play_again != 'yes':
                print("Game over! Thanks for playing.")
                break
            else:
                continue