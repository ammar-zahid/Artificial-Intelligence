#If the names of 2 friends are same; what will happen to the program in problem 6?

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

# it only prints the first key and its value of the same name