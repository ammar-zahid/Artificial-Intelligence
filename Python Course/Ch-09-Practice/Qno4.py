# a file contains "donkey" word multiple times. write a program which replace this word with "#####" in the same file

word = "donkey"
buzzWord = "######"

with open("word_file.txt") as f:
    content = f.read()

with open("word_file.txt", 'w') as f:
    newContent = content.replace(word, buzzWord)
    f.write(newContent)