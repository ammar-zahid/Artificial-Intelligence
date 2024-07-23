# Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique.

dictt = {}

name = input("Enter your name : ")
lang = input("Enter your favorite language : ")
dictt.update({name : lang})
name = input("Enter your name : ")
lang = input("Enter your favorite language : ")
dictt.update({name : lang})
name = input("Enter your name : ")
lang = input("Enter your favorite language : ")
dictt.update({name : lang})
name = input("Enter your name : ")
lang = input("Enter your favorite language : ")
dictt.update({name : lang})

print(dictt)