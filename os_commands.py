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

print('Good bye!')


# input streams
data = input("This will come from STDIN: ")
print("We we write it to STDOUT: " + data + 1)
print("Now we generate an error to STDERR: " + data + 1)







