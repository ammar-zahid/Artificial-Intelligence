# Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.

phy_marks = int(input("Enter physics marks : "))
chem_marks = int(input("Enter chemistry marks : "))
math_marks = int(input("Enter maths marks : "))

per = (100 * (phy_marks + chem_marks + math_marks)/300)

if(per >= 33 and per <= 100):
    print(f"Passed : {per}")
else:
    print(f"Failed : {per}")