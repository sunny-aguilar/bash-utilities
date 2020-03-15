#!/usr/bin/python3
import sys              # access command line args
import os

def create_python_script():
    comments = '################################################\n'\
                '# Author:          Sandro Aguilar\n'\
                '################################################'

    print(sys.argv[1])

    with open(sys.argv[1]) as file:
        file.write(comments)

# call function
create_python_script()


# print('Num of args:', len(sys.argv), 'arguments.')
# print('Arg list:', str(sys.argv))
