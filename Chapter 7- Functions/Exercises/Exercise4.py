# make_shirt() function where shirt size is large by default with a message that reads 'I love Python'.
def make_shirt(size="large", message="I love Python"):
    print(f"Size {size} T-shirt with the message '{message}'.")

# A large shirt with the default message
make_shirt()

# A medium shirt with the default message
make_shirt(size="medium")

# A shirt of any size with a different message
make_shirt(size="small", message='My love for you has no bugs')