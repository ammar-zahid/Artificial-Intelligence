# Write a program to print the following star pattern: 
"""

*
**
***

"""

n = int(input("Enter a number : "))

for i in range(1, n+1):
    print("*" * i)