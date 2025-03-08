class Cell:
    
    def __init__(self, is_alive: bool = False) -> None:
        #self.is_alive = alive #?
        self.is_alive = is_alive        #instance variable

        #self.neighbors
        #self.location
    
    def set_alive(self) -> None:
        """ Sets the cell to be alive."""
        self.is_alive = True

    def set_dead(self) -> None:
        """ Sets the cell to be dead """
        self.is_alive = False

    def is_alive(self) -> bool:
        """ Returns whether or not the cell is alive """
        return self.is_alive