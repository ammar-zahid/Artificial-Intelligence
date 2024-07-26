"""
print this using recursion
*****
****
***
**
*
"""

def pattern(n):
    if(n==0):
        return ""
    current_line = "*"*n
    return current_line + "\n" + pattern(n-1)

pattern_print = pattern(5)
print(f"{pattern_print}")