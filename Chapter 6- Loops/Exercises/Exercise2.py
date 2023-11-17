# Loop in which you ask users their age, and then tell them the cost of their movie ticket

prompt="what is your age?"
prompt+="\nEnter 'quit' when you wish to stop."
while True:
    age=input(prompt)
    if age=='quit':
        break
    age=int(age)
    if age < 3:
        print("  You are allowed to enter for free!")
    elif age < 13:
        print("  Your ticket will coat $10.")
    else:
        print("  Your ticket will cost $15.")