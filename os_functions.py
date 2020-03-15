#!/usr/bin/python3
import os
import datetime

txt = "Current working dir: {}"
print(txt.format(os.getcwd()))

txt = "File size: {}"
print(txt.format(os.path.getsize('text_file')))

timestamp = os.path.getmtime("text_file")
datetime.datetime.fromtimestamp(timestamp)
datetime.datetime(2020, 1, 6, 7, 2, 3 899999)
