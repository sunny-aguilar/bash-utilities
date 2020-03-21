#!/usr/bin/python3
####################################################################
# Author:               Sandro Aguilar
# Date:                 Month day, 2020
# Class:                Coursera
# Description:          Using Python to interact with the Operating
#                       system. This program uses the CSV module to
#                       perform various operations on CSV files
#                       such as printing.
####################################################################
import csv

f = open('csv_file.csv')
csv_f = csv.reader(f)

for row in csv_f:
    name, phone, role = row
    print("Name: {}, Phone: {}, Role: {}".format(name, phone, role))

f.close()

# store data into a csv file
hosts = [["workstation.local", "192.165.25.46"], ["webserver.cloud", "10.2.5.6"]]

with open('csv_file.csv', 'w') as hosts_csv:
    writer = csv.writer(hosts_csv)
    writer.writerows(hosts)

# dicreader to process CSV files with header row
with open('csv_file.csv') as software:
    reader = csv.DictReader(software)
    for row in reader:
        print(('{} has {} users').format(row['name'], row['users']))

users = [{"name": "Sol Mansi", "username": "solm", "department": "IT infrastructure"},
        {"name": "Lio Nelson", "username": "lion", "department": "User Experience Research"},
        {"name": "Charlie Grey", "username": "greyc", "department": "Development"}]

keys = ['name', 'username', 'department']

with open('by_department.csv', 'w') as by_department:
    writer = csv.DictWriter(by_department, fieldnames=keys)
    writer.writeheader()
    writer.writerows(users)

