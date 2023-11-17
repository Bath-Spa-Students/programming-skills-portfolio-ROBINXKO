# Function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.
# Program for the function to print a sentence summarizing the size of the shirt and the message printed on it.
def make_shirt(size, message):
    print(f"Size {size} T-shirt with the message '{message}'.")

# call the function using positional arguments to make a shirt
make_shirt("medium", "Ha Ha Ha Ha")

# Call the function using keyword arguments to mnake a shirt
make_shirt(size="large", message="Be yourself;everyone else is already taken")