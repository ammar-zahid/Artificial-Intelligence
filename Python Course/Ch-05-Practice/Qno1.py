# Write a program to create a dictionary of Hindi words with values as their English translation. Provide user with an option to look it up!

language = {
    "paani" : "water",
    "sabzi" : "vegetable",
    "kheera" : "cocumber",
    "pankha" : "fan"
}

lafz = input("""Kis lafz ka english meaning dekhna chahte ho ?
1. paani
2. sabzi
3. kheera
4. pankha\n""")

print(language.get(lafz))