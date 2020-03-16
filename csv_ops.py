#!/usr/bin/python3
####################################################################
# Author:              Sandro Aguilar
# Date:                Month day, 2020
# Class:               CS XXX
# Description:         Enter description here
#                      
#                      
#                      
####################################################################
import csv

f = open('csv_file.csv')
csv_f = csv.reader(f)

for row in csv_f:
    name, phone, role = row
    print("Name: {}, Phone: {}, Role: {}".format(name, phone, role))

f.close()