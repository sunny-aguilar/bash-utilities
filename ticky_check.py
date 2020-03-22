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
        #print(parsed_row)
        regex_info = r"INFO(\s)*([\w ]*)"
        regex_error = r"ERROR(\s)*([\w ]*)"
        info_results = re.search(regex_info, parsed_row)
        error_results = re.search(regex_error, parsed_row)
        if info_results is not None:
            #print(results)
            print(info_results[0])
            #print(results[1])
            if info_results[0] not in error_message:
                error_message[info_results[0]] = 0 + 1
            else:
                error_message[info_results[0]] += 1

print("")
print(Error Message Dictionary:)
print(error_message)












