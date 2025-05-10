"""#CSV 
# csv.DictReader("filename") 
# csv.DictWriter("filename, fieldnames")
# csv.reader("filename")
# csv.writer("filename")
#writer.writerows()
#writer.writerow("data")"""
# Inventory Management System
import csv
import uuid
class InventoryItem:
    def __init__(self, item_id, name, quantity, price):
        self.item_id = item_id
        self.name = name
        self.quantity = quantity
        self.price = price
        self.sku = str(uuid.uuid4())
    def display_info(self):
        print(f"Item ID: {self.item_id}, Name: {self.name}, Quantity: {self.quantity}, Price: ${self.price:.2f}, Sku: {self.sku}" )
class InventoryManger:
    def __init__(self, file):
        self.file = file
        self.inventory = []
        self.next_item_id = 0


    def update_item(self):
        pass
    def load_inventory(self):
        try:
            with open(self.file, 'r') as file:
              reader = csv.DictReader(file)
              self.inventory = [InventoryItem(int(item['item_id']), 
                                              item['name'], 
                                              int(item['quantity']), 
                                              float(item['price']))
                                                for item in reader]
              self.next_item_id = len(self.inventory) + 1
        except FileNotFoundError:
            print(f"File {self.file} not found. Starting with an empty inventory.")

        #Save to csv file

    def add_item(self, name, quantity, price):
        row = InventoryItem(self.next_item_id, name, quantity, price)
        self.inventory.append(row)
        self.next_item_id += 1
        self.save_inventory()
        # save to csv file

    def save_inventory(self):
        with open(self.file, 'w', newline='') as file:
            fieldnames = ['item_id', 'name', 'quantity', 'price', 'sku']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(
                {
                'item_id': row.item_id,
                'name': row.name,
                'quantity': row.quantity,
                'price': row.price,
                'sku': row.sku,
                }
            for row in self.inventory
            )  

    def display_inventory(self):
        if not self.inventory:
            print("Inventory is empty.")
        else:
            for items in self.inventory:
                items.display_info()

    def delete_item_by_id(self, item_id):
        self.inventory = [row for row in self.inventory if row.item_id != item_id]
        self.save_inventory()
        
    def filter_item(self, max_price):
        return [row for row in self.inventory if row.price <= max_price]
    

def main():
    store = InventoryManger("Inventory.csv")
    store.load_inventory()
    while True:
        print("\nInventory Management System")
        print("1. Add Item")
        print("2. Display Inventory")
        print("3. Delete Item")
        print("4. Filter Items by Price")
        print("5. Saving Invetory")
        print("6. Exit\n")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter item name: ")
            quantity = int(input("Enter item quantity: "))
            price = float(input("Enter item price: "))
            store.add_item(name, quantity, price)

        elif choice == '2':
            store.display_inventory()

        elif choice == '3':
            item_id = int(input("Enter item ID to delete: "))
            store.delete_item_by_id(item_id)

        elif choice == '4':
            max_price = float(input("Enter maximum price: "))
            filtered_items = store.filter_item(max_price)
            print(f"Items with price less than or equal to {max_price}:")
            for items in filtered_items:
                items.display_info()

        elif choice == '5':
            store.save_inventory()
            print("Saving inventory to file...")

        elif choice == '6':
            print("Goodbye!")
            break


        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main() 
    # This code is a simple inventory management system that allows you to add, display, delete, and filter items in the inventory.