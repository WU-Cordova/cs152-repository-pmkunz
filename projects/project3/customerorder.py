from orderitem import OrderItem
from datastructures.linkedlist import LinkedList

class CustomerOrder:
    
    def __init__(self, customer_name: str):
        """ Initalizes an new order with the customer's name """
        self.customer_name = customer_name
        self.items = LinkedList(data_type = OrderItem)

    def add_item(self, order_item: OrderItem) -> None:
        """ Adds an OrderItem object (drink and customization) to the order """
        self.items.append(order_item)

    def __str__(self) -> str:
        """ Returns a string representation of the customer order 
        (human-readable) """
        items_str = "\n".join(f"- {item}" for item in self.items)
        return f"📝 Order Summary for {self.customer_name}:\n{items_str}"

    def __repr__(self) -> str: 
        """ Returns a string representation of the customer order
        (offical string represenation) """
        return f"CustomerOrder(customer_name='{self.customer_name}', items={repr(self.items)})"