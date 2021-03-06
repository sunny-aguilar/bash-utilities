#!/usr/bin/python3
####################################################################
# Author:               Sandro Aguilar
# Date:                 March 21, 2020
# Class:                Coursera - final project
# Description:          Final project for course
####################################################################
import re
import operator


regex = r"ticky: INFO: ([\w ]*) "
line = "May 27 11:45:40 ubuntu.local ticky: INFO: Created ticket [#1234] (username)"
print(re.search(r"ticky: INFO: ([\w ]*) ", line))

line = "May 27 11:45:40 ubuntu.local ticky: ERROR: Error creating ticket [#1234] (username)"
print(re.search(r"ticky: ERROR: ([\w ]*) ", line))


fruit = {"oranges": 3, "apples": 5, "bananas": 7, "pears": 2}
print(sorted(fruit.items()))    # sorted by keys
print(sorted(fruit.items(), key=operator.itemgetter(0)))    # sort by keys
print(sorted(fruit.items(), key=operator.itemgetter(1)))    # sort by values
print(sorted(fruit.items(), key = operator.itemgetter(1), reverse=True))    # reverse sort


















