#!/usr/bin/python3
import os

def create_python_script(filename):
    comments = "# Start of a new Python program"
    file = open(filename, 'w+')
    file.write(comments)
    file.close()

    file_size = os.path.getsize('program.py')
    #print(file_size)
    return(file_size)

print(create_python_script("program.py"))
