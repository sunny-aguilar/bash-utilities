#!/usr/bin/python3
####################################################################
# Author:               Sandro Aguilar
# Date:                 Month day, 2020
# Class:                Coursera: Using Python to interact with the OS
# Description:          Managing data and processes.
####################################################################

# input function to prompt for user input
# name = input('Please enter your name: ')
# print("Hello, " + name + '.')


def to_seconds(hours, minutes, seconds):
    return hours*3600 + minutes * 60 + seconds

cont = 'y'
# while (cont.lower() == 'y'):
#     hours = int(input('Enter the number of hours: '))
#     minutes = int(input('Enter the number of minutes: '))
#     seconds = int(input('Enter the number of seconds: '))
#     print("That's {} seconds".format(to_seconds(hours, minutes, seconds)))
#     print()
#     cont = input('do you want to do another conversion? [y to continue] ')

#print('Good bye!')


# input streams
# data = input("This will come from STDIN: ")
# print("We we write it to STDOUT: " + data)
# print("Now we generate an error to STDERR: " + data + 1)


# get environment variables
# import os

# print("HOME: " + os.environ.get("HOME", ""))
# print("HOME: " + os.environ.get("SHELL", ""))
# print("HOME: " + os.environ.get("FRUIT", "NOT PRESENT"))



# how to determine if command line instructions succeeded or failed
# import sys
# print(sys.argv)

# command-line arguments
# import os
# import sys

# filename=sys.argv[1]

# if not os.path.exists(filename):
#     with open(filename, 'w') as f:
#         f.write('New file created\n')
# else:
#     print('Error, the file {} already exists!'.format(filename))
#     sys.exit(1)



# Python subprocesses
# import subprocess
# subprocess.run(['date'])
# subprocess.run(['sleep', '1'])
# result = subprocess.run(['ls', 'this_file'])
# print(result.returncode)


# obtaining the output of a system command
# result = subprocess.run(['host', '8.8.8.8'], capture_output=True)
# print(result)
# print(result.stdout.decode().split())

# result = subprocess.run(['rm', 'does_not_exist'], capture_output=True)
# print(result.returncode)
# print(result.stdout)
# print(result.stderr)

# advanced subprocess management
# import os
# import subprocess

# my_env = os.environ.copy()          # copy environment variables to pass to child
# my_env['PATH'] = os.pathsep.join(['/opt/myapp/', my_env['PATH']])
# result = subprocess.run(['myapp'], env=my_env)



# filtering logs files with regular expressions
import re

pattern = r'USER \((\w+)\)$'
line = 'Jul 6 14:04:02 computer.name CRON[29440]: USER (naughty user)'
result = re.search(pattern, line)
print(result[1])


















