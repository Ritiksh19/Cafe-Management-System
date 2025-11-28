#Define the menu of restaurant 
menu = {
    'pizza': 40,
    'Pasta': 60,
    'Burger': 40,
    'salad': 20,
    'coffee': 80,
    'Water': 20,
}


#Greet
print("Welcome to PYHTON Restaurant")
print("pizz: Rs40\nPasta: Rs60\nBurger: Rs40\nSalad: Rs20\nCoffee: Rs80\nWater: Rs20\n")

order_total = 0
#80 + 70 = 150

Item_1 = input("Enter the name of item you want to order = ")
if Item_1 in menu:
    order_total += menu[Item_1]
    print(f"Your item {Item_1} has been added to your order")

else:
    print(f"ordered item {Item_1} is not avaialable yet!")

another_order = input("Do you want to add another item? (Yes/No) ")
if another_order == "Yes":
    Item_2 = input("Enter the name of sucond item = ")
    if Item_2 in menu:
        order_total += menu[Item_2]
        print(f"item {Item_2} has been added to order")
    else:
        print(f"Ordered item {Item_2} is not avaialable!")

print(f"The total amount of items to pay is {order_total}")            
