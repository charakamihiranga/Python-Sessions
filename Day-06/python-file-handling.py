#Reading Files in Python

# Open a file
# file = open("my_file.txt", "r") # "r" represent the mode of file action  ( read mode is the default mode of file actions)
# Read the contents of the file

# read_content = file.read()

# read_content = file.readline() # display the content from current cursor position to first "\n" (next line character)

# read_content = file.readlines() # display the content from current cursor position to last "\n" (next line character) this return a list of lines

# file.close()

# print(read_content) 
# print(type(read_content)) # <class, 'str'>

#Different modes to open a file
# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists
# "t" - Text - Default value. Text mode
# "b" - Binary - Binary mode (e.g. images)
# "r+" - Read/Write - Opens a file for reading and writing, error if the file does not exist
# "a+" - Append and Read - Opens a file for appending and reading, creates the file if it does not exist
# "w+" - Write and Read - Opens a file for writing and reading, creates the file if it does not exist
# "x+" - Create and Read - Creates the specified file, returns an error if the file exists
# "t+" - Text and Read/Write - Text mode for reading and writing
# "b+" - Binary and Read/Write - Binary mode for reading and writing (e.g. images)


## 'with' statement for file handling (standard)

with open("my_file.txt", "r") as file:
    read_content = file.read()
    print(read_content)

# no need for file.close() when using 'with' statement it automatically close the file after the block of code is executed    