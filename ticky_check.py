#!/usr/bin/env python3
####################################################################
# Author:               Sandro Aguilar
# Date:                 March 21, 2020
# Class:                Coursera - final project
# Description:          Parses log files to to count the types of
#                       errors encountered. It also maintains a
#                       count of the users interacting with the
#                       system and types of logs tracked for each
#                       user.
####################################################################
import re
import operator
import csv


# parse syslogs and create dictionaries
def parse_logs(error_message, user_count, error_tracker):
    with open('sys.log') as file:
        for row in file:
            parsed_row = row.strip()
            regex_error = r"ERROR(\s)*([\w ]*)"
            results_error = re.search(regex_error, parsed_row)

            if results_error is not None:
                if results_error.group(0) not in error_message:
                    error_message[results_error[0]] = 0 + 1
                else:
                    error_message[results_error[0]] += 1


            # add data to user error type list
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

                        user_count[results_user] = [results_user, 0 , 0]
                        user_count[results_user][1] += 1
                    else:
                        user_count[results_user][1] += 1

            # find 'ERROR' and store user stats in dictionary
            elif results_TYPE[0] == "ERROR":
                if results_user is not None:
                    #? debugging - show usernames and type of syslog interaction
                    # print(results_user + " : " + results_TYPE[0])
                    if results_user not in user_count:
                        user_count[results_user] = [results_user, 0, 0]
                        user_count[results_user][2] += 1
                    else:
                        user_count[results_user][2] += 1


# create CSV file with sorted message data
def create_csv(file_name, data):
    # create CSV file and create column names
    with open(file_name, 'w') as error_file:
        writer = csv.writer(error_file)
        writer.writerows(data)
        # for key, value in data.items():
        #     writer.writerow([key, value])

# create CSV file with sorted error data
def create_csv_user(file_name, data):
    with open(file_name, 'w', newline='') as user_file:
        writer = csv.writer(user_file)
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

    # save sorted dictionaries
    sorted_m = {}
    sorted_u = {}

    # save sorted dictionary in a new dict to keep sort
    sorted_msg = sorted(error_message.items(), key=operator.itemgetter(1), reverse=True)
    sorted_msg.insert(0, ("Error", "Count"))


    # save sorted dictionary in a new dict to keep sort
    sorted_user = sorted(user_count.items())
    for item in sorted_user:
        sorted_u[item[0]] = item[1]

    sorted_u_list = []
    for item in sorted_u:
        sorted_u_list.append(sorted_u.get(item))

    sorted_u_list.sort()
    sorted_u_list.insert(0, ["Username", "INFO", "ERROR"])



    # create CSV files
    create_csv('error_message.csv', sorted_msg)
    create_csv_user('user_statistics.csv', sorted_u_list)




# start program
main()
