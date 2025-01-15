sandwich_orders = ["Grilled Cheese","Egg Sandwich","Ice Cream Sandwich","Pastrami","Ham Sandwich","Pastrami","Pastrami","Chicken Sandwich","BLT Sandwich","Po'boy"]
finished_sandwiches = []
x = 0
print("ATTENTION: Unfortunately, the deli has recently run out of Pastrami stock. All orders of Pastrami will hereby be nullified.")

while "Pastrami" in sandwich_orders:
    sandwich_orders.remove("Pastrami")
while x < len(sandwich_orders):
    item = sandwich_orders[x]
    print("The "+ str(item) +" is ready!")
    finished_sandwiches.append( sandwich_orders.pop(sandwich_orders.index(item))) 
print("Sandwiches made today: " + str(finished_sandwiches))
