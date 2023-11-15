# Store the locations in a list.
places_to_visit = ['Yellowstone national park', 'Tokyo', 'kyoto', 'Saudi Arabia', 'Netherlands']

# Print the list in its original order.
print(f"Original order: {places_to_visit}\n")

# Use sorted() to print the list in alphabetical order.
print(f"Alphabetical order: {sorted(places_to_visit)}")

# Show that the list is still in its original order.
print(f"The list is still in its original order: {places_to_visit}\n")

# Use sorted() to print the list in reverse alphabetical order.
print(f"Reverse alphabetical order: {sorted(places_to_visit, reverse=True)}")

# Show that the list is still in its original order.
print(f"The list is still in its original order: {places_to_visit}\n")

# Use reverse() to change the order of the list.
places_to_visit.reverse()
print(f"List after first reverse(): {places_to_visit}")

# Use reverse() to change the order of the list again.
places_to_visit.reverse()
print(f"List after second reverse(): {places_to_visit}")

# Use sort() to change the list so it's stored in alphabetical order.
places_to_visit.sort()
print(f"List after sort(): {places_to_visit}")

# Use sort() to change the list so it's stored in reverse alphabetical order.
places_to_visit.sort(reverse=True)
print(f"List after sort(reverse=True): {places_to_visit}\n")