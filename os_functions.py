#!/usr/bin/python3
import os
import datetime

txt = "Current working dir: {}"
print(txt.format(os.getcwd()))

txt = "File size: {}"
print(txt.format(os.path.getsize('text_file')))

timestamp = os.path.getmtime("text_file")

