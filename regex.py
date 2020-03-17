#!/usr/bin/python3
####################################################################
# Author:              Sandro Aguilar
# Date:                Month day, 2020
# Class:               Coursera Regex
# Description:         Intro to regular expressions in Python
####################################################################
import re               #regex module

log = 'July 31 97:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade'
regex = r"\[(\d+)\]"
result = re.search(regex, log)
print(result[1])



# /usr/share/dict/words
# . a dot matches any character (wildcard)
#   grep s.ing file.txt
# -i on grep means search regardless of case
# ^ begin search at the beginning of line i.e. grep ^fruit file.txt
# $ search at end of a line grep car$ file.txt

# raw strings - always use raw string for regex
result = re.search(r'aza', 'plaza')
print(result)

result = re.search(r'aza', 'bazaar')
