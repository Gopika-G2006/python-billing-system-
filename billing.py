menu = {"Burger": 50,  # Burger costs 50
        "Juice": 30}

name = input("Enter customer name: ")
phone = input("Enter phone no: ")
customer = [name, phone]

print("\n MENU")
for item, price in menu.items():
    print(f"{item}:{price}")

item1 = input("\nEnter first item (Burger or Juice): ")
qty1 = int(input("Enter quantity: "))
item2 = input("\nEnter second item (Burger or Juice): ")
qty2 = int(input("Enter quantity: "))

Total_item1 = menu[item1] * qty1
Total_item2 = menu[item2] * qty2
Final = Total_item1 + Total_item2

print("\n BILL")
print(f"Customer Name: {customer[0]}")
print(f"Phone Number: {customer[1]}")
print(f"{item1} x {qty1} = {Total_item1}")
print(f"{item2} x {qty2} = {Total_item2}")
print(f"Total Amount: {Final}")
