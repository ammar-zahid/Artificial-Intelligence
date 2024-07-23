# relational operators --> >= , <= , ==
# logical operators --> and , or , not

age = int(input("Enter your age : "))

if(age > 19):
    print("You are an adult")
elif(age <= 19 and age > 0):
    print("You are a teenager")
else :
    print("error")
