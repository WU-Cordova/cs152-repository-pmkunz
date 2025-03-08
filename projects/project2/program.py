
from projects.project2.grid import Grid
from projects.project2.kbhit import KBHit
from projects.project2.gamecontroller import GameController

# I run it and the file path doesn't work, but then I enter this in the terminal and it will work:
# export PYTHONPATH=/Users/pkmckenna/Documents/GitHub/cs152-repository-pmkunz:$PYTHONPATH


def main():
    grid = Grid(10, 10)
    game_controller = GameController(grid)
    game_controller.run(100)

if __name__ == '__main__':
    main()
