# file = open("data.txt", 'r')
# file_data = file.read()
# print(file_data)
# file.close()

string = 'This is input data injected by python file'

file = open("data.txt", 'w')
file_data = file.write(string)
print(file_data)
file.close()