#!/usr/bin/env python3
####################################################################
# Author:               Sandro Aguilar
# Date:                 March 21, 2020
# Class:                Coursera - final
# Description:          Enter description here
####################################################################
import re
import operator
import csv

error_message = {}
user_count = {}

with open('sys.log') as file:
    for row in file:
        parsed_row = row.strip()
        print(parsed_row)
        regex_info = r"INFO(\s)*([\w ]*)"
        regex_error = r"ERROR"
        results = re.search(regex_error, parsed_row)
        if results is not None:
            print(results)
            print(results[0])
            print(results[1])













