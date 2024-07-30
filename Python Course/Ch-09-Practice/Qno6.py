# find a line number in file where 'python' word is located

with open("findpython.txt") as f:
    lines = f.readlines()
    line_no = 1
    for line in lines:
        if("python" in line):
            print(f"Line no is {line_no}")
        line_no += 1