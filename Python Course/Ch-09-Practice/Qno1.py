# Write a program to read the text from a given file ‘poems.txt’ and find out whether it contains the word ‘twinkle’.

with open('Qno1.txt') as file:
    content = file.read()
    if('Twinkle' in content or 'twinkle' in content):
        print("Twinkle is present in poem")
    else:
        print("Twinkle is not present in poem")