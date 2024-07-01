#display contents of cart with total price of contents
def display_cart(cart):
    if not cart:
        print("Your cart is empty")
    else:
        print("Shopping cart: " )
    total_price = 0
    for item in cart:
        print(f"{item['name']}: ${item['price']}")
        total_price += item['price']
    print(f"Total: ${total_price:.2f}")

#adds an item to the cart list    
def add_to_cart(cart):
    item_name = input("Enter item name: ")
    item_price = float(input("Enter item price: "))
    item = {"name": item_name, "price": item_price}
    cart.append(item)
    print("Item added to cart")
    
#removes an items from the cart
def remove_from_cart(cart):
    #if cart is empty, print message and return to menu
    if not cart:
        print("Your cart is already empty")
    # removes an indiviudal item from the cart
    else:
        display_cart(cart)
        item_index = int(input("Enter the item number to remove: ")) - 1
        if 0 <= item_index < len(cart):
            removed_item = cart.pop(item_index)
            print(f"Removed item: {removed_item['name']}")
        else:
            print("Invalid item number.")
#clears current cart with clear built-in function 
def clear_cart(cart):
    if not cart:
        print("Your cart is already empty")
    else:
        display_cart(cart)
        clear_input = input("Do you want to clear cart? (y/n): ")
        if clear_input.lower() == "y":
            cart.clear()
            print("Cart cleared")
        elif clear_input.lower() == "n": 
            print("Cart not cleared")
        else:
            print("Invalid choice. Please type 'y' or 'n'.")
     
def display_menu():
    print("1. Add to cart")
    print("2. Display cart")
    print("3. Remove from cart")
    print("4. Clear cart")
    print("5. Quit")       
def main():
    cart = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            add_to_cart(cart)
        elif choice == "2":
            display_cart(cart)
        elif choice == "3":
            remove_from_cart(cart)
        elif choice == "4":
            clear_cart(cart)
        elif choice == "5":
            print("Exiting application...")
            break
        else:
            print("Invalid choice")

            
if __name__ == "__main__":
    main()

