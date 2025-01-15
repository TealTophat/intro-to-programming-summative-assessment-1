sandwich_orders = ["Grilled Cheese","Egg Sandwich","Ice Cream Sandwich","Ham Sandwich","Chicken Sandwich","BLT Sandwich","Po'boy"]
finished_sandwiches = []
x = 0

while x < len(sandwich_orders):
    item = sandwich_orders[x]
    print("The "+ str(item) +" is ready!")
    finished_sandwiches.append( sandwich_orders.pop(sandwich_orders.index(item))) 
print("Sandwiches made today: " + str(finished_sandwiches))
