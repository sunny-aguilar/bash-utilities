#!/usr/bin/python3
import os

txt = "Current working dir: {}"
print(txt.format(os.getcwd()))

txt = "File size: {}"
print(txt.format(os.path.getsize('text_file')))
