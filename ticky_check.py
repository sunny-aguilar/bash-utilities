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
            #print(results_error[0])
            #print(results[1])
            if results_error[0] not in error_message:
                error_message[results_error[0]] = 0 + 1
            else:
                error_message[results_error[0]] += 1

        #regex_message = r'[A-Z]{4}[A-Z]*(\s)*([\w ]*)'
        #regex_info_message = r"INFO(\s)*([\w ]*)"


        regex_info = r"INFO"
        results_info = re.search(regex_info, parsed_row)
        regex_error = r"ERROR"
        results_error = re.search(regex_error, parsed_row)
        regex_TYPE = r"[A-Z]{4}.?"
        results_TYPE = re.search(regex_TYPE, parsed_row)


        regex_all = r"[A-Z]{4}.*"
        results_all = re.search(regex_all, parsed_row)

        regex_user = r"\([\w.]*\)$"
        results_user = re.search(regex_user, parsed_row)


        # if username is found, parse message
        if results_user is not None:
            if results








        # if results_user is not None:
        #     print("Username: " + results_user[0])

        #     # if user is not in user_count dictionary
        #     if results_user[0] not in user_count:
        #         #user_count[results_user[0]] = 0 + 1

        #         # find INFO in log
        #         results_info = re.search(regex_info, parsed_row)
        #         if results_info is not None:
        #             #print("INFO: " + results_info[0])
        #             if results_info[0] not in user_count:
        #                 print("INFO: " + results_info[0])
        #                 user_count[results_user[0]] = 0 + 1
        #             # else:
        #             #     user_count[results_user[0]] += 1

        #     else:
        #         # find INFO in log
        #         results_info = re.search(regex_info, parsed_row)
        #         if results_info is not None:
        #             if results_info[0] not in user_count:
        #                 print("INFO: " + results_info[0])
        #                 user_count[results_user[0]] = 0 + 1
        #             else:
        #                 user_count[results_user[0]] += 1

                #user_count[results_user[0]] += 1

print()
print("Error Message Dictionary:")
print(error_message)
print()
print("User Usage Dictionary:")
print(user_count)
print()










