#Label the program written in problem 4 with comments.

import os

# Select the directory whose content you want to list 
directory_path = 'D:\Code\Artificial Intelligence\Python Course'

# Use the os module to list the directory content 
contents = os.listdir(directory_path)

# Print the contents of the directory 
print(contents)