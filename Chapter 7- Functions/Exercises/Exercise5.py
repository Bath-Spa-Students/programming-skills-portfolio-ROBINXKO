# Function called describe_city() that accepts the name of a city and its country. The parameter for the country is given a default value.
# Program for the function should print a simple sentence, such as Reykjavik is in Iceland.
def describe_city(city,country="Saudi arabia"):
    print(f'The city of {city} is in {country}.')

#Call the function for three different cities
describe_city('Riyadh')      #This one uses default
describe_city('Beijing','China')
describe_city('Brasília','Brazil')