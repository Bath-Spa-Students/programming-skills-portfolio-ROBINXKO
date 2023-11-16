# Several dictionaries representing different pets
pet1 = {
    'animal': 'cat',
    'owner': 'Jeseem'
}

pet2 = {
    'animal': 'dog',
    'owner': 'Hafeez'
}

pet3 = {
    'animal': 'rabbit',
    'owner': 'Fayiz'
}

# The dictionaries in a list called pets
pets = [pet1, pet2, pet3]

# Program to Loop through the list and print everything about each pet
for pet in pets:
    print(f"{pet['owner']} has a {pet['animal']}.")