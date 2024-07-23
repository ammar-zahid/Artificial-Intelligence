# Write a program to find whether a given username contains less than 10 characters or not.

name = input("Enter your name : ")
name_len = len(name)

if(name_len > 10):
    print("Name has more than 10 characters")
elif(name_len == 10):
    print("Name has 10 characters")
elif(name_len > 0 and name_len < 10):
    print("Name has less than 10 characters")
else:
    print("Error")