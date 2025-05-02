from bistrosystem import BistroSystem
from drink import Drink

###########
# MUST ENTER THIS INTO TERMINAL FOR CODE TO RUN:
# export PYTHONPATH=/Users/pkmckenna/Documents/GitHub/cs152-repository-pmkunz:$PYTHONPATH


def main():
    system = BistroSystem()

    # 5 drinks on the menu
    system.add_menu_item(Drink("Bearcat Mocha", 4.50))
    system.add_menu_item(Drink("Caramel Catpuccino", 4.25))
    system.add_menu_item(Drink("Meowcha Latte", 4.75))
    system.add_menu_item(Drink("Vanilla Purrccino", 4.00))
    system.add_menu_item(Drink("Espresso Whisker Shot", 3.50))

    while True:
        print("\n📋 Main Menu")
        print("1. Display Menu")
        print("2. Take New Order")
        print("3. View Open Orders")
        print("4. Mark Next Order as Complete")
        print("5. End-of-Day Report")
        print("6. Exit")

        choice = input("\nEnter your choice: ").strip()

        ###########
        if choice == "1":
            system.display_menu()

        ###########
        elif choice == "2":
            name = input("\nWhat's your name? ").strip()

            try:
                num_drinks = int(input("How many drinks would you like to order? ").strip())
                if num_drinks <= 0:
                    print("Please enter a positive number.")
                    continue
            except ValueError:
                print("Invalid number.")
                continue

            items = []
            for i in range(1, num_drinks + 1):
                while True:
                    try:
                        drink_num = int(input(f"\nDrink #{i}: Enter drink number (1-5): ").strip())
                        if not (1 <= drink_num <= len(system.menu)):
                            print("Invalid drink number. Try again.")
                            continue
                        break
                    except ValueError:
                        print("Please enter a number.")

                customization = input(f"Any customization for {system.menu[drink_num - 1].name}? ").strip()
                items.append((drink_num - 1, customization))

            # Preview the order
            print(f"\n📝 Order Summary for {name}:")
            for idx, cust in items:
                drink = system.menu[idx]
                summary = f"{drink.name} ({drink.size})"
                if cust:
                    summary += f" - {cust}"
                print(f"- {summary}")

            # Confirmation of order
            confirm = input("\nConfirm order? (yes/no): ").strip().lower()
            if confirm == "yes":
                system.take_order(name, items)
                print("\n✅ Order placed successfully!")
            else:
                print("\n❌ Order canceled.")

        ###########
        elif choice == "3":
            print("\n🕒 Open Orders:")
            if system.open_orders.empty:
                print("No open orders.")
            else:
                for i, order in enumerate(system.open_orders, start=1):
                    print(f"\nOrder #{i}:")
                    print(order)

        ###########
        elif choice == "4":
            system.complete_order()

        ###########
        elif choice == "5":
            system.print_end_of_day_summary()

        ###########
        elif choice == "6":
            print("Goodbye!")
            break

        ###########
        else:
            print("Invalid option. Please select a number from 1 to 6.")

if __name__ == "__main__":
    main()

