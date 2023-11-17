# List of sandwich orders with 'pastrami' appearing at least three times
sandwich_orders = ['club', 'samuna', 'pastrami', 'peanut butter', 'pastrami', 'falafel', 'tuna', 'pastrami']

# An empty list to store finished sandwiches
finished_sandwiches = []

# A message about running out of pastrami
print("Sorry, deli has run out of pastrami.\n")

# Remove all occurrences of 'pastrami' from sandwich_orders
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

# Loop to move made sandwiches from sandwich_orders to the list of finished_sandwiches
# Message for each order
while sandwich_orders:
    current_order = sandwich_orders.pop() 
    print(f"The {current_order} sandwich order is ready.")
    finished_sandwiches.append(current_order)

# The list of finished sandwiches
print("\nList of finished sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich + " sandwich")