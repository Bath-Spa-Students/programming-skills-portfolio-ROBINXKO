# glossary dictionary
glossary = {
    'for loop': 'A programming structure that repeats a sequence of instructions.',
    'f-string':'f-string is a feature that allows you to embed expressions inside string literals, using curly braces. The expressions are replaced with their values',
    'string': 'A sequence of characters, such as letters or numbers.',
    'List': 'A collection of items in a particular order. Items in a list can be accessed by their index. Lists are mutable, which means you can change their contents.',
    'Variables': 'They are like containers or memory locations that can hold different types of data, such as numbers, strings, or even objects.'
}

# Program to print each word and its meaning in a neatly formatted output
for word, meaning in glossary.items():
    print(f"{word}:")
    print(f"{meaning}\n")