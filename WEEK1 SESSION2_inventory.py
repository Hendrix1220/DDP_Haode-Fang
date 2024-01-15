
items={"apple":4}
    
def add_item(item):
        if item in items:
            newquantity=int(input("How many you want to add:"))
            items[item]+=newquantity

        else:
            quantity=int(input("How many you want to add:"))
            items[item]=quantity
        return items
    # Implementation Instructions:
    # 1. Check if the item exists in the inventory dictionary.
    # 2. If it does, increase its quantity.
    # 3. If not, add the item to the inventory with the given quantity.
pass

# Function to view all items in the inventory
def view_inventory(item):
        if item in items:
            return items[item]
        else:
            print("not found")
    # Implementation Instructions:
    # 1. Loop through the inventory dictionary.
    # 2. Print each item's name and its quantity.
pass

# Function to update the quantity of an existing item in the inventory
def update_item(item):

        if item in items:
            newquantity=int(input("How many you want to add:"))
            items[item]=items[item]+newquantity
        else:
            print("not found")
        return items
    # Implementation Instructions:
    # 1. Check if the item exists in the inventory.
    # 2. If it does, update its quantity.
    # 3. If the item doesn't exist, print a message indicating it's not found.
pass

# Main function to manage the inventory
def manage_inventory():
    while True:
        print("\nInventory Management System")
        print("1. Add Item")
        print("2. View Inventory")
        print("3. Update Item Quantity")
        print("4. Exit")
        choice = input("Enter choice (1/2/3/4): ")
            
        if choice == "1":
                name=input("provide the item: ")
                print(add_item(name))
        elif choice=="2":
                name=input("provide the item: ")
                print(view_inventory(name))
        elif choice=="3":
                name=input("provide the item: ")
                print(update_item(name))
    


        # Process the user's choice
        # Implementation Instructions:
        # 1. If the choice is '1', prompt the user to enter an item name and quantity,
        #    and then call the add_item function.
        # 2. If the choice is '2', call the view_inventory function.
        # 3. If the choice is '3', prompt the user to enter an item name and new quantity,
        #    and then call the update_item function.
        # 4. If the choice is '4', break the loop to exit the program.
        # 5. For any other input, display an error message.
        pass

# Entry point of the program
if __name__ == "__main__":
    manage_inventory()