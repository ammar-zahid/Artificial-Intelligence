# replace words with #### in list of words

words = ["donkey", "ganday", "bad"]
buzzWord = "#"

with open("word_file.txt", 'r') as f:
    content = f.read()

with open("word_file.txt", 'w') as f:
    for word in words:
        if(word in content):
            content = content.replace(word, buzzWord * len(word))
    f.write(content)