

class Drink:

    def __init__(self, name: str, price: float):
        """ Initializes a Drink object iwth a name, size and price """
        self.name = name
        self.size = "Medium" # Fixed size
        self.price = price
    
    def __str__(self):
        """ Returns a string representation of the drink 
        (human-readable) """
        return f"{self.name} ({self.size}) - ${self.price:.2f}" # 2f means the float will show 2 digits after the decimal

    def __repr__(self):
        """ Returns a string representation of the drink
        (offical string represenation) """
        return f"Drink(name='{self.name}', price = {self.price})"
