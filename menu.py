# Define a menu with food items and their prices
menu = {
    "Pizza": 8.99,
    "Burger": 5.49,
    "Pasta": 7.99,
    "Salad": 4.49,
    "Soda": 2.33,
}

# Function to display the menu
def display_menu():
    print("Menu:")
    for item, price in menu.items():
        print(f"{item}: ${price:.2f}")
    print()

# Function to take order from the customer
def take_order():
    order = {}
    total_price = 0.0
    
    while True:
        display_menu()
        item = input("Enter the food item you want to order (or type 'done' to finish): ").capitalize()
        
        if item == 'Done':
            break
        
        if item in menu:
            quantity = int(input(f"How many {item}(s) would you like to order? "))
            order[item] = quantity
            total_price += menu[item] * quantity
        else:
            print("Sorry, we don't have that item. Please choose from the menu.")
    
    return order, total_price

# Function to display the bill
def display_bill(order, total_price):
    print("\n----- Your Bill -----")
    for item, quantity in order.items():
        print(f"{item} x{quantity}: ${menu[item] * quantity:.2f}")
    print("----------------------")
    print(f"Total: ${total_price:.2f}")
    print("Thank you for your order!")

# Main program
def main():
    print("Welcome to our Restaurant!")
    order, total_price = take_order()
    display_bill(order, total_price)

# Run the main program
if __name__ == "__main__":
    main()
