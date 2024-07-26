# file = open("data.txt")
# lines = file.readlines()
# print(lines, type(lines))
# file.close()


# line = file.readline()
# print(line)
# line = file.readline()
# print(line)
# line = file.readline()
# print(line)
# line = file.readline()
# print(line)
# line = file.readline()
# print(line)
# file.close()

file = open("data.txt")
line = file.readline()
while(line != ""):
    print(line)
    line = file.readline()