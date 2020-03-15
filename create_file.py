#!/usr/bin/python3
import sys              # access command line args
import os

def create_python_script():
    comments = '####################################################################\n'\
                '# Author:              Sandro Aguilar\n'\
                '# Date:                Month day, 2020\n'\
                '# Class:               CS XXX\n'\
                '# Description:         Enter description here\n'\
                '#                      \n'\
                '#                      \n'\
                '#                      \n'\
                '####################################################################\n'



    with open(sys.argv[1], 'w+') as file:
        file.write(comments)

# call function
create_python_script()


# print('Num of args:', len(sys.argv), 'arguments.')
# print('Arg list:', str(sys.argv))
