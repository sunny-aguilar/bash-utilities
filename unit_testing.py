#!/usr/bin/python3
####################################################################
# Author:               Sandro Aguilar
# Date:                 March 20, 2020
# Class:                Coursera - Unit Testing
# Description:          Testing in Python (unit tests)
####################################################################
import re

def rearrange_name(name):
    result = re.search(r'^([\w .]*), ([\w .]*)$', name)
    if result is None:
        return name
    return '{} {}'.format(result[2], result[1])




















