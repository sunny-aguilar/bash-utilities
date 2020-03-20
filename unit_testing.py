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


# Errors and Exceptions
def validate_user(username, minlen):
    assert type(username) == str, 'username must be a string'
    if minlen < 1:
        raise ValueError('minlen must be at least 1')
    if len(username) < minlen:
        return False
    if not username.isalnum():
        return False
    return True

if (validate_user('Sunny', 0)):
    print("validated")












