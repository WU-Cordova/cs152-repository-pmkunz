
import random
from character import Character

class Game:
    """Manages the Dice Battle game logic."""

    def __init__(self, player1: Character, player2: Character):
            """Initializes the game with two players."""
            self.player1 = player1
            self.player2 = player2

    def attack(self, attacker: Character, defender: Character):
        """Performs an attack where the attacker rolls a die to determine damage dealt."""
        die_roll = random.randint(1, 6)

        #...

    def start_battle(self):
        """Starts a turn-based battle between two players."""
        turn = 1

        if turn % 2 != 0:
            attacking_player = self.player1
            defending_player = self.player2
        else:
            attacking_player = self.player2
            defending_player = self.player1

        #...

        # Switch turns
        turn += 1