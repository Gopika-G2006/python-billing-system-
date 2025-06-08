# python-billing-system-
Description

This Python program simulates a simple food billing system for a small café or restaurant. It allows the user to input customer details and order quantities for selected menu items, then calculates and displays the final bill.

Features

Displays a menu with item names and prices.

Accepts customer name and phone number as input.

Takes orders for two items and their quantities.

Calculates the total cost for each item and the final bill.

Prints a detailed bill with customer information and order summary.


How to Run

1. Make sure you have Python installed on your computer.


2. Save the program code into a file named billing.py (or any name you prefer).


3. Open your terminal or command prompt and navigate to the folder where the file is saved.


4. Run the program by typing:

python billing.py


5. Follow the on-screen prompts to enter customer details and order items.



Code Example

Here’s a small snippet from the program:

menu = {"Burger": 50, "Juice": 30}

name = input("Enter customer name: ")
phone = input("Enter phone no: ")

print("\n MENU")
for item, price in menu.items():
    print(f"{item}: {price}")

item1 = input("\nEnter first item (Burger or Juice): ")
qty1 = int(input("Enter quantity: "))
# ...

Future Improvements

Add more items to the menu.

Allow ordering more than two items.

Implement input validation for item names and quantities.

Save bills to a file for record keeping.
