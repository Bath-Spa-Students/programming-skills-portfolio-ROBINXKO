# List of guests.
great_minds=['Albert einstein','Nikola tesla','Isaac newton']

# Message inviting them for dinner.
for guest in great_minds:
    print(f"Sir {guest}, it gives me great pleasure to invite you to dinner at my residence. I look forward for a positive reponse from you.")

# Print call stating the name of the guest who can't make it for dinner.
print(f"\nUnfortunately sir {great_minds[2]}, can't make it due to health problems.\n")

# Modifing the list, replacing the name of the guest who can’t make it with the name of the new person i am inviting.
great_minds[2]='J. Robert Oppenheimer'

# New set of invitation meassages. One for each person who is still in my list.
for guest in great_minds:
    print(f"Sir {guest}, it gives me great pleasure to invite you to dinner at my residence. I look forward for a positive reponse from you")

# Pop guests from my list until only two are left.
while len(great_minds) > 2:
    popped_guest = great_minds.pop()
    print(f"\nSir {popped_guest}, I am very sorry to inform you that I am unable to invite you to dinner because there is insufficient space to accomodate you.\n")

# Print invite message to each of the two people still on my list.
for guest in great_minds:
    print(f"Hello, sir {guest}.")
    print(f"I would like to respecfully invite you to dinner at my residence.")

# Usimg del to remove the last two names from my list.
del great_minds[0]
del great_minds[0]

# Print the list to make sure it is empty.
print(f"\nMy guest list is now: {great_minds}")