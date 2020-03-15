#!/usr/bin/python3
import os
import datetime

txt = "Current working dir: {}"
print(txt.format(os.getcwd()))

txt = "File size: {}"
print(txt.format(os.path.getsize('text_file')))

timestamp = os.path.getmtime("text_file")
datetime.datetime.fromtimestamp(timestamp)
print(datetime.datetime(2020, 1, 6, 7, 2, 3, 899999))

print(os.path.exists('text_file'))

# os.mkdir('new_dir')
# os.chdir('new_dir')
# os.rmdir('new_dir')

print(os.listdir('./bash-utilities'))

