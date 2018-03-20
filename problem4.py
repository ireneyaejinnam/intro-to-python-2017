#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 17:00:54 2017

@author: ireneyaejinnam
"""

def pizza():
    
    size = input("Small, medium, or large? ")
    return  "a {} pizza with {}".format(size, toppings())

def toppings():
   
    choice = ""
    final_topping = []
    while choice != "done":
        choice = input("Add a topping: pepperoni, mushrooms, spinach, or say 'done'. ")
        if choice == "done":
            break
        else:
            final_topping.append(choice)
    topping = " and ".join(final_topping)
    if final_topping == []:
        topping = "no topping"
    return topping
    
def salad():
    
    salad_choice = input("Would you like a garden salad or greek salad? ")
    dressings = dressing()
    salad_order = "a {} salad with {} dressings"
    return  salad_order.format(salad_choice, dressings)
               
def dressing():
    
    return input("please choose a dressing: vinaigrette, ranch, blue cheese, lemon. ")

def select_meal():

    choice = ""
    full_order = []
    while choice != "done":
        choice = input("Hello, would you like pizza or salad? ")
        if choice == "pizza":
            full_order.append(pizza())
        elif choice == "salad":
            full_order.append(salad())
        elif choice == "done":
            break
        order = " and ".join(full_order)
        print ("You ordered "+order+". Place another order or say 'done': ")
    print("Your order has been placed. Goodbye.")
    
select_meal()