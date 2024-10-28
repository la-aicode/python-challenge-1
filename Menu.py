# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}
menu_dashes = "-" * 42
# Initialize the order list
order = []

# Launch the store and present a greeting to the customer
print("Welcome to the variety food truck.")

# Main loop for ordering
while True:
    # Display main menu
    print("\nWhich menu would you like to view? ")

    # Initialize the menu item number and store categories
    i = 1
    menu_items = {}

    # Display menu categories and store in menu_items dictionary
    for key in menu.keys():
        print(f"{i}: {key}")
        menu_items[i] = key
        i += 1

    # Get menu category selection
    menu_selection = input("Type menu number to view or q to quit: ")

    # Check for exit condition
    if menu_selection.lower() == 'q':
        break

    # Check if menu_selection is a valid number
    if not menu_selection.isdigit():
        print("Please enter a valid number.")
        continue

    # Convert menu_selection to an integer
    menu_selection = int(menu_selection)

    # Check if menu_selection is within menu items
    if menu_selection not in menu_items:
        print("Selection not in menu options.")
        continue

    # Get the selected category name
    menu_category_name = menu_items[menu_selection]
    print(f"\nYou selected {menu_category_name}")

    # Display selected category items
    print(menu_dashes)
    print(f"This is the {menu_category_name} menu.")
    print(menu_dashes)
    print("Item # | Item name                | Price")
    print("-------|--------------------------|-------")

    # Dictionary to store items in the selected category
    category_items = {}
    item_counter = 1

    # Display items and prices, add to category_items for selection
    for key, value in menu[menu_category_name].items():
        if isinstance(value, dict):
            for sub_key, sub_value in value.items():
                item_name = f"{key} - {sub_key}"
                category_items[item_counter] = (item_name, sub_value)
                print(f"{item_counter}      | {item_name:<24} | ${sub_value:.2f}")
                item_counter += 1
        else:
            category_items[item_counter] = (key, value)
            print(f"{item_counter}      | {key:<24} | ${value:.2f}")
            item_counter += 1

    print(menu_dashes)

    # Get user’s item selection
    menu_selection = input("Enter item number to order: ")

    # Validate item selection as a number
    if not menu_selection.isdigit():
        print("Please enter a valid item number.")
        continue

    # Convert menu_selection to an integer
    menu_selection = int(menu_selection)

    # Check if menu_selection is in the category items
    if menu_selection not in category_items:
        print("Invalid item selection.")
        continue

    # Extract item name and price
    item_name, item_price = category_items[menu_selection]

    # Prompt for quantity with default to 1 if input is invalid
    quantity = input("Enter quantity (default is 1): ")
    if not quantity.isdigit() or int(quantity) <= 0:
        quantity = 1
    else:
        quantity = int(quantity)

    # Add the item to the order list in dictionary format
    order.append({"item": item_name, "price": item_price, "quantity": quantity})
    print(f"Added {quantity} x {item_name} to your order.")

    # Ask if the customer would like to continue ordering
    continue_ordering = input("Would you like to keep ordering? (y/n): ").lower()
    if continue_ordering == 'y':
        continue
    elif continue_ordering == 'n':
        break
    else:
        print("Invalid response. Returning to menu.")

# Display the final order summary if items were ordered
if order:
    print("\nYour Order Summary:")
    print("Item name                 | Price  | Quantity")
    print("--------------------------|--------|----------")

    # Calculate total price using list comprehension
    total_cost = sum([item["price"] * item["quantity"] for item in order])

    # Display each item with specified formatting
    for item in order:
        # Extract item details
        item_name = item["item"]
        item_price = item["price"]
        quantity = item["quantity"]
        
        # Print formatted receipt row
        print(f"{item_name:<26}| ${item_price:<6.2f}| {quantity:<9}")

    # Print total cost
    print("--------------------------|--------|----------")
    print(f"{'Total cost':<26}| ${total_cost:.2f}")
else:
    print("No items were ordered.")



