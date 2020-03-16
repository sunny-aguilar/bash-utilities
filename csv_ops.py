#!/usr/bin/python3
####################################################################
# Author:               Sandro Aguilar
# Date:                 Month day, 2020
# Class:                Coursera
# Description:          Using Python to interact with the Operating
#                       system. This program uses the CSV module to
#                       perform various operations on CSV files
#                      such as printing.
####################################################################
import csv

f = open('csv_file.csv')
csv_f = csv.reader(f)

for row in csv_f:
    name, phone, role = row
    print("Name: {}, Phone: {}, Role: {}".format(name, phone, role))

f.close()