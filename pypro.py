# DEFINE the menu of restaurant.
menu={
    'burger':50,
    'pizza':100,
    'pasta':80,
    'snadwitch':60,
    'salad':40,
    'soup':30
}
print("Welcome to the restaurant!")
print("Here is the menu:")
for item, price in menu.items():
    print(f"{item}: {price}")
print("Please enter the items you want to order, separated by commas.")
order = input("Enter your order: ").split(",")
print("Your order is:")
for item in order:
    item = item.strip()  # Remove leading/trailing whitespace
    if item in menu:
        print(f"{item}: {menu[item]}")
    else:
        print(f"{item} is not available in the menu.")
print("Thank you for your order!")
print("Your total bill is:")
total_bill = 0
for item in order:
    item = item.strip()  # Remove leading/trailing whitespace
    if item in menu:
        total_bill += menu[item]
print(total_bill)