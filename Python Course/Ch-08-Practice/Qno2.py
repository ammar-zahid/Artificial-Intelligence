#write a recursive function to print the sum of n natural numbers

def sum(n):
    if(n==1):
        return 1
    return n + sum(n-1)

ans = sum(10)
print(f"{ans}")