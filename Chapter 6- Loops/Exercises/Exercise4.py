# List called sandwich_orders filled with the names of various sandwiches
sandwich_orders=['falafel sandwich','samuna sandwich','peanut butter sandwich','tuna sandwich','club sandwich']

# Empty list called finished_sandwiches
finished_sandwiches=[]

# Loop to move made sandwiches from sandwich_orders to the list of finished_sandwiches
# Message for each order
while sandwich_orders:
    current_order = sandwich_orders.pop()
    print("The " + current_order + " order is ready.")
    finished_sandwiches.append(current_order)

# Message listing each sandwich that was made
print("\nList of finished sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)