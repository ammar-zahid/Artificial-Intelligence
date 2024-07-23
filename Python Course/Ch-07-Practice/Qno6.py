# Write a program to calculate the factorial of a given number using for loop.

n = int(input("Enter a number : "))
fact = 1
for i in range(1, n+1):
    fact = fact * i

print(f"Factorial is {fact}")
# 5! = 5 x 4 x 3 x 2 x 1