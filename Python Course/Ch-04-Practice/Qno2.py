# Write a program to accept marks of 6 students and display them in a sorted manner.

marks = []

st1 = int(input("Enter Marks: "))
st2 = int(input("Enter Marks: "))
st3 = int(input("Enter Marks: "))
st4 = int(input("Enter Marks: "))
st5 = int(input("Enter Marks: "))
st6 = int(input("Enter Marks: "))

marks.append(st1)
marks.append(st2)
marks.append(st3)
marks.append(st4)
marks.append(st5)
marks.append(st6)

marks.sort()
print(marks)
