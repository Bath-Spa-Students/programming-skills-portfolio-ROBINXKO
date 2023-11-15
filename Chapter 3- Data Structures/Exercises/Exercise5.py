# List of guests.
great_minds = ['Albert einstein', 'Nikola tesla' , 'Isaac newton']

# Message inviting them for dinner.
for guest in great_minds:
    print(f"Sir {guest}, it gives me great pleasure to invite you to dinner at my residence. I look forward for a positive reponse from you.")

# Print call stating the name of the guest who can't make it for dinner.
print(f"Unfortunately sir {great_minds[1]}, can't make it due to health problems.")

# Modifing the list, replacing the name of the guest who can’t make it with the name of the new person i am inviting.
great_minds[1]='J. Robert Oppenheimer'

# New set of invitation meassages. One for each person who is still in my list.
for guest in great_minds:
    print(f"sir {guest}, it gives me great pleasure to invite you to dinner at my residence. I look forward for a positive reponse from you")