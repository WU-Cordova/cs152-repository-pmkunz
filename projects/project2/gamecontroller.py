from projects.project2.grid import Grid
from projects.project2.kbhit import KBHit
import time

class GameController:

    def __init__(self, grid: Grid) -> None:
        #print("from the constructor")
        self.grid = grid
        self.kb = KBHit()
        self.running = True
        self.auto_mode = True 

    def choose_mode(self) -> bool:
        """ Choose automatic mode or manual mode """
        print("Welcome to the Game of Life!")
        mode = input("Would you like the game to run in automatic mode? (y/n)").strip.lower()
        
        # return mode == "y"  # Will return True if it does, False if it doesn't

        if mode == "y":
            self.auto_mode = True
        else:
            self.auto_mode = False

    def run(self, generations: int) -> None:

        generation_count = 0

        while self.running:

            self.grid.display()		# runs function from grid.py

            if self.grid.is_stable():
                print("Grid is stable. Ending simulation.")
                break
            
            if self.auto_mode:
                time.sleep(1)
            else:
                print("Press any key to continue onto the next generation.")
                if self.kb.kbhit():
                    self.kb.getch()
            self.grid.next_generation()

            generation_count += 1

    def quit_game(self) -> None:
        """ Quit the game """
        print("Thanks for playing!")
        self.running = False