
# Importing Data Structures:
from datastructures.array import Array
from datastructures.circularqueue import CircularQueue
from datastructures.bag import Bag
from datastructures.hashmap import HashMap

# Importing Classes:
from drink import Drink
from orderitem import OrderItem
from customerorder import CustomerOrder

class BistroSystem:
    """ Main system: manages menu, orders, and end-of-day summaries """

    def __init__(self):
        self.menu = Array(data_type=Drink)
        self.open_orders = CircularQueue(maxsize=100, data_type=object)
        self.completed_orders = Bag()
        self.sales_summary = HashMap()

    def add_menu_item(self, drink: Drink) -> None:
        """ Adds a drink to the menu """
        self.menu.append(drink)

    def display_menu(self) -> None:
        """ Prints the current menu """
        print("🍹 Bearcat Bistro Menu:")
        for i in range (len(self.menu)):
            print(f"{i+1}. {self.menu[i]}")

    def take_order(self, customer_name: str, item_indices_customizations: list[tuple[int, str]]) -> None:
        """ Takes a new order for a customer """

        order = CustomerOrder(customer_name)

        for idx, customization in item_indices_customizations:
            if idx < 0 or idx >= len(self.menu):
                raise IndexError("Invalid menu index.")
            drink = self.menu[idx]
            order_item = OrderItem(drink, customization)
            order.add_item(order_item)

        self.open_orders.enqueue(order)
        print(f"{customer_name}'s order placed.")

    def complete_order(self) -> None:
        """ Completes the next order in the queue.
        Moves it to completed orders and updates the sales summary """

        if self.open_orders.empty:
            print("No open orders.")
            return

        order = self.open_orders.dequeue()
        self.completed_orders.add(order)

        # Update sales summary
        for item in order.items:
            name = item.drink.name
            price = item.drink.price
            if name in self.sales_summary:
                quantity, total = self.sales_summary[name]
                self.sales_summary[name] = (quantity + 1, total + price)
            else:
                self.sales_summary[name] = (1, price)

        print(f"✅ Completed order for {order.customer_name}.")

    def print_end_of_day_summary(self) -> None:
        """ Displays the total sales and quanttieis by drink """

        print("\n📊 End-of-Day Report:")
        print("-" * 28)
        print(f"{'Drink Name':<24}Qty Sold   Total Sales")
        total_revenue = 0

        # Iterate over the sales summary to print the report
        for name, (quantity, total) in self.sales_summary.items():
            print(f"{name:<24}{quantity:<10}{f'${total:.2f}'}")
            total_revenue += total

        print(f"{'Total Revenue:':<34}{f'${total_revenue:.2f}'}")