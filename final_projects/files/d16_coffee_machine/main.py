from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import time
import os

def check_input(prompt,condition,err_msg):
    while True:
        try:
            ans=input(prompt)
            if not condition(ans): raise ""
            break
        except:
            print(err_msg)
            continue
    return ans

drinks=Menu()
machine=CoffeeMaker()
money=MoneyMachine()

while True:
    print("Hello! ",end="")
    dr = check_input(
        prompt = f"What would you like to drink? {'/'.join(drinks.get_items())}\n",
        condition = lambda x: 
            (x.strip().lower() in drinks.get_items()) or 
            (x == 'off') or 
            (x == 'report'),
        err_msg = "Sorry that item is not available.").strip().lower()

    if dr == "off":
        print("switching off...")
        time.sleep(1)
        os._exit(0)
    elif dr == "report":
        machine.report()
        money.report()
        continue
    else:
        drink = drinks.get_drink(dr)
        if machine.is_resource_sufficient(drink):
            print(f"Please insert ${drink.cost}.")
            if money.make_payment(drink.cost):
                machine.make_order(drink)
        print("="*100)
        continue
