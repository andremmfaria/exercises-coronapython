# 7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. As they enter each topping, print a message saying you’ll add that topping to their pizza.

pizza_toppings = []

active = True
while active:
    message = input("\nPlease enter pizza toppings: \n")
    if message == 'quit':
        active = False
        
    else:
        pizza_toppings.append(message)
        
print(pizza_toppings)