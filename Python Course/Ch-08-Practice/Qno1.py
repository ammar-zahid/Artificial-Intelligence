#write a program to find the greatest of three numbers using functions

n1 = input("Enter n1: ")
n2 = input("Enter n2: ")
n3 = input("Enter n3: ")

def find_greatest(n1, n2, n3):
    if(n1>n2 and n1>n3):
        return n1
    if(n2>n1 and n2>n3):
        return n2
    if(n3>n2 and n3>n1):
        return n3
    

ans = find_greatest(n1, n2, n3)
print(f"Greatest is {ans}")