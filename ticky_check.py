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

with open('user_emails.csv') as software:
    reader = csv.DictReader(software)
    for row in reader:
        print(('{} has {} users').format(row['name'], row['users']))





















