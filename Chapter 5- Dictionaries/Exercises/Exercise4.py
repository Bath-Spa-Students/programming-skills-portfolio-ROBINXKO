# Dictionary containing three major rivers and the country each river runs through.
rivers = {
    'Nile': 'Egypt',
    'Amazon': 'Brazil',
    'Volga': 'Russia'
}

# loop to print a sentence about each river
for river, country in rivers.items():
    print(f"The {river} river runs through {country}.")

# loop to print the name of each river included in the dictionary
print("\nThe rivers in the dictionary:")
for river in rivers.keys():
    print(river)

# loop to print the name of each country included in the dictionary
print("\nThe countries in the dictionary:")
for country in rivers.values():
    print(country)