import random
from character import Character
from charactertype import CharacterType

class Game:
    """Manages the Dice Battle game logic."""

    def __init__(self, player1: Character, player2: Character):
        """Initializes the game with two players."""
        # self.player1 = player1
        # self.player2 = player2

        self.player1: Character = player1
        self.player2: Character = player2

    def attack(self, attacker: Character, defender: Character):
        """Performs an attack where the attacker rolls a die to determine damage dealt."""
        die_roll = random.randint(1, 6)     # Random number between 1 and 6
        defender.health -= die_roll * attacker.attack_power
        print(f"{attacker.name} attacks {defender.name} and does {die_roll} damage.")
        print(f"{defender.name} now has {max(0, defender.health)} health remaining. \n")

    def start_battle(self):
        """Starts a turn-based battle between two players."""
        
        print(f"Battle Start: {self.player1.name} vs {self.player2.name}\n")

        turn = 1                                        # Start with the first turn

        while self.player1.health > 0 and self.player2.health > 0:
            if turn % 2 != 0:                           # Odd-numbered turns
                self.attack(self.player1, self.player2)
            else:                                       # Even-numbered turns
                self.attack(self.player2, self.player1)

            turn += 1                                   # Switch turns

        winner: Character = self.player1 if self.player1.health > 0 else self.player2
        print(f"{winner.name} wins the battle!")