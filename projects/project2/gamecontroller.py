from projects.project2.grid import Grid
from projects.project2.kbhit import KBHit
import time
import os

class GameController:

    def __init__(self, grid: Grid) -> None:
        """ Constructor """
        self.grid = grid
        self.kb = KBHit()
        self.running = True
        self.auto_mode = False 

    def run(self, generations: int) -> None:

        while True:

            generation_count = 0
            key = None

            while self.running:

                os.system('cls' if os.name == 'nt' else 'clear')

                self.grid.display()		# runs function from grid.py

                if self.grid.is_stable():
                    print("Grid is stable. Ending simulation.")
                    self.running = False
                    break
                
                if self.auto_mode:
                    print("Enter 'a' for automatic mode, 'm' for manual mode, 's' to continue onto the next generation, or 'q' to quit.")
                    time.sleep(1)   # 1 second delay when displaying the new generation
                    self.grid.next_generation()
                    
                    if self.kb.kbhit():
                        key = self.kb.getch()
                        if key.lower() == 'm':  # Switch to manual mode
                            self.auto_mode = False
                        elif key.lower() == 'q':  # Quit the game
                            print("Thanks for playing!")
                            self.running = False
                            break

                else: # manual mode
                    print("Enter 'a' for automatic mode, 'm' for manual mode, 's' to continue onto the next generation, or 'q' to quit.")

                    while not self.kb.kbhit():
                        time.sleep(0.1)
                    
                    key = self.kb.getch()

                    if key: #checks if key was pressed
                        if key.lower() == 'a':
                            self.auto_mode = True
                        elif key.lower() =='m':
                            self.auto_mode = False
                        elif key.lower()=='s':
                            self.grid.next_generation()
                        elif key.lower() == 'q':
                            print("Thanks for playing!")
                            self.running = False
                            break
                        else:
                            print("Invalid key. Enter 'a' for automatic mode, 'm' for manual mode, 's' to continue onto the next generation, or 'q' to quit.")
                        
                generation_count += 1

            if self.restart_or_quit():  #if this returned True
                self.grid = Grid(self.grid.width, self.grid.height)
                self.running = True
            else:
                print("Exiting the program. Thanks for playing!")
                break

    def restart_or_quit(self) -> bool:
        """ Offers the user a chance to start a new simulation or quit the program"""

        answer = None

        print("\nSimulation has ended.")
        print("Would you like to start a new simulation (n) or quit (q)? ")

        while True:

            while not self.kb.kbhit():
                time.sleep(0.1)

            answer = self.kb.getch()

            if answer:
                if answer == 'n':
                    return True     
                elif answer == 'q':
                    return False
                else:
                    print("Invalid key. Enter 'n' to start a new simulation or 'q' to quit.")