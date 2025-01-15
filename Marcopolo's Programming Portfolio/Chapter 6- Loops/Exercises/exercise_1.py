topping = input("What topping do you want to add to this pizza?\n")

while topping != "quit":
    print("Great! I will add this "+topping+" to the pizza.")
    topping = input("What other toppings do you want to add to the pizza?\nIf you wish to end the process, type 'quit.'\n")
else:
    print("That's a nice pizza you've got there!")