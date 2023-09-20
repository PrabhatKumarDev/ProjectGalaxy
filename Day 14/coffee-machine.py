#import coffee data from data.py
from data import data

#import logo from the art.py
from art import logo 

# import os module
import os

# clear terminal
def clear():
    os.system('cls')

# Print the report of the items available
def report(water,milk,coffee,money):
    print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${money}")

def place_order(water, milk, coffee,data,money):
    which_coffee=input("What would you like? (espresso/latte/cappuccino): ")
    if(which_coffee=="report"):
        report(water,milk,coffee,money)
        money=float("%.2f"%money)
        return water,milk,coffee,money,True
    else:
        no_of_quarters=int(input("How many quarters?: "))
        no_of_dimes=int(input("How many dimes?: "))
        no_of_nickles=int(input("How many nickles?: "))
        no_of_pennies=int(input("How many pennies?: "))   
        total_amount_1=total_amount(no_of_quarters,no_of_dimes,no_of_nickles,no_of_pennies)
        type=coffee_type(which_coffee);
        # If total amount is greater than or equal to price of the coffee placed and all items are available.
        if(total_amount_1>=data[type]["price"] and water>=data[type]["water"] and milk >= data[type]["milk"] and coffee >= data[type]["coffee"]):
            change = total_amount_1-data[type]["price"]
            change=float("%.2f"%change)
            water=water-data[type]["water"]
            milk=milk-data[type]["milk"]
            coffee=coffee-data[type]["coffee"]
            print(f"Here is ${change} in change")
            print(f"Here is your {data[type]['item']} ☕. Enjoy!")
            money+=data[type]["price"]
            money=float("%.2f"%money)
            return water,milk,coffee,money,True
        # If any item is unavailable for coffee type
        elif(water < data[type]["water"] or milk < data[type]["milk"] or coffee < data[type]["coffee"]):
            clear()
            print("Sorry 😔 Not enough quantity at machine")
            money=float("%.2f"%money)
            return 0,0,0,0,False
        # If total amount is less than price of the coffee
        elif(total_amount_1<data[type]["price"]):
            print(f"Sorry that's not enough money. Money refunded.")
            money=float("%.2f"%money)
            return water,milk, coffee,money,True
    
# Return number on the type of the coffee 
def coffee_type(which_coffee):
    if(which_coffee=="espresso"):
        return 0
    elif(which_coffee=="latte"):
        return 1
    elif(which_coffee=="cappuccino"):
        return 2
    
# Return the total amount of the coins given by the uesr
def total_amount(no_of_quarters,no_of_dimes,no_of_nickles,no_of_pennies):
    quarters=0.25;
    dimes=0.10;
    nickles=0.05;
    pennies=0.01;   
    total_amount=(no_of_dimes*dimes) + (no_of_quarters * quarters) + (no_of_nickles*nickles)+(no_of_pennies*pennies)
    return total_amount

# Item Quantity avaialble
water=300
milk=200
coffee=200
money=0
not_end=True

# Print the logo
print(logo)
# Loop run while not_end=True
while not_end:
    quantity=place_order(water,milk, coffee, data,money)
    water=quantity[0]
    milk=quantity[1]
    coffee=quantity[2]
    money=quantity[3]
    not_end=quantity[4]