from drink import Drink

class OrderItem:

    def __init__(self, drink: Drink, customization: str = ""):
        """ Initalizes an OrderItem object with a Drink as well as optional customization """
        self.drink = drink
        self.customization = customization

    def __str__(self) -> str:
        """ Returns a string representation of the order item 
        (human-readable) """

        if self.customization:
            return f"{self.drink.name} ({self.drink.size}) - {self.customization}"
        else:
            return f"{self.drink.name} ({self.drink.size})"

    def __repr__(self) -> str:
        """ Returns a string representation of the order item
        (offical string represenation) """

        return f"OrderItem(drink={repr(self.drink)}, customization='{self.customization}')"