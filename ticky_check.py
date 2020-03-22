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
        regex_error = r"ERROR(\s)*([\w ]*)"
        
        results_error = re.search(regex_error, parsed_row)
        

        if results_error is not None:
            #print(results)
            print(results_error[0])
            #print(results[1])
            if results_error[0] not in error_message:
                error_message[results_error[0]] = 0 + 1
            else:
                error_message[results_error[0]] += 1

        regex_user = r"\([\w.]*\)$"
        regex_user = r"\([\w.]*\)$"regex_info = r"INFO(\s)*([\w ]*)"
        regex_message = r'[A-Z]{4}[A-Z]*(\s)*([\w ]*)'

        user_results = re.search(regex_user, parsed_row)
        results_info = re.search(regex_info, parsed_row)
        if user_results is not None:
            print(user_results[0])
            if user_results[0] not in user_count:
                user_count[user_results[0]] = 0 + 1
            else:
                user_count[user_results[0]] += 1

print()
print("Error Message Dictionary:")
print(error_message)
print()
print("User Usage Dictionary:")
print(user_count)
print()










