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


# parse syslogs and create dictionaries
def parse_logs(error_message, user_count, error_tracker):
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

            #regex_user = r"\([\w.]*\)$"
            #results_user = re.search(regex_user, parsed_row)
            regex_user = r"\((.*?)\)"
            results_user = re.search(regex_user, parsed_row).group(1)

            # find 'INFO' and store user stats in dictionary
            if results_TYPE[0] == "INFO ":
                if results_user is not None:
                    #? debugging - show usernames and type of syslog interaction
                    # print(results_user + " : " + results_TYPE[0])
                    if results_user not in user_count:
                        user_count[results_user] = [0, 0]
                        user_count[results_user][0] += 1
                    else:
                        user_count[results_user][0] += 1

            # find 'ERROR' and store user stats in dictionary
            elif results_TYPE[0] == "ERROR":
                if results_user is not None:
                    #? debugging - show usernames and type of syslog interaction
                    # print(results_user + " : " + results_TYPE[0])
                    if results_user not in user_count:
                        user_count[results_user] = [0, 0]
                        user_count[results_user][1] += 1
                    else:
                        user_count[results_user][1] += 1


# create CSV files with sorted data
def create_csv(file_name, data):
    # create errors CSV file
    keys = ['Error', 'Count']
    data = [{'Error': "wrong", 'Count': '5'}, {'Error': 'mess up', 'Count': 3}]
    # create CSV file and create column names
    with open(file_name, 'w') as error_file:
        writer = csv.DictWriter(error_file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)


# start program
def main():
    # data dictionaries
    error_message = {}
    user_count = {}
    error_tracker = {}

    # get syslog files and create dictionaries
    parse_logs(error_message, user_count, error_tracker)

    # save sorted dictionaries
    sorted_msg = {}
    sorted_user = {}

    # debugging - show sorted dictionaries
    print()
    print("Error Message Dictionary:")
    # save sorted dictionary in a new dict to keep sort
    sorted_msg = sorted(error_message.items(), key=operator.itemgetter(1), reverse=True)
    print(sorted_msg)
    print()
    print("User Usage Dictionary:")
    # save sorted dictionary in a new dict to keep sort
    sorted_user = sorted(user_count.items())
    print(sorted_user)
    print()

    # create CSV files
    create_csv('error_message.csv', sorted_msg)






# start program
main()









