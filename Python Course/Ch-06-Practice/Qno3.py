# A spam comment is defined as a text containing following keywords: “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program to detect these spams.

keyword = input("Enter keyword : ")

if(keyword == "Make a lot of money" or keyword == "buy now" or keyword == "subscribe this" or keyword == "click this"):
    print("Spam keyword detected")
else:
    print("No spam keyword detected")