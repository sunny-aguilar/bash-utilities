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
print(result)

result = re.search(r'aza', 'maze')
print(result)       # returns None meaning no match found

print(re.search(r'^x', 'xenon'))

print(re.search(r'p.ng', 'penguin'))
print(re.search(r'p.ng', 'clapping'))
print(re.search(r'p.ng', 'sponge'))

# case insensitive
print(re.search(r'p.ng', 'Pangaea', re.IGNORECASE))

# my test using variables holding strings
txt = "sandro"
print(re.search(r'ndr', txt))

# character classes []
print(re.search(r'[Pp]ython', 'python'))

# a range of characters using a dash [-]
print(re.search(r'[A-Z]ack', 'jack'))
print(re.search(r'[a-z]ack', 'jack'))
print(re.search(r'[a-zA-Z0-9]ack', '9ack'))     # combine multiple ranges at once
print(re.search(r'[^a-z]ack', '4ack'))          # not in a range

# find one expression or the other pipe |
print(re.search(r'cat|dog', 'I like cats.'))
print(re.search(r'cat|dog', 'I like dogs.'))
print(re.search(r'cat|dog', 'I like both dogs and cats.'))

# find all returns all instances
print(re.findall(r'cat|dog', 'I like both dogs and cats.'))

# repeated matches  .* (zero or more occurences of anything)
print(re.search(r'Py.*n', 'Pygmalion'))
print(re.search(r'Py.*n', 'Python Programming'))
print(re.search(r'Py[a-z]*n', 'Python Programming'))

# +: 1 or more occurrences of the character that comes before it
print( re.search( r'o+l+', 'goldfish' ) )
print( re.search( r'o+l+', 'woolly' ) )
print( re.search( r'o+l+', 'boil' ) )           # returns none

# ?: 0 or 1 occurrences of the character before it
print(re.search(r'p?each', 'To each their own'))

# escaping characters \
print(re.search(r'\.com', 'www.suny.com'))
rs = '\.com'
print(re.search(rs, 'www.suny.com'))

# capturing groups ()
result = re.search(r'^(\w*), (\w*)$', 'Lovelace, Ada')
print(result)
print(result.groups())
print(result[0])
print(result[1])
print(result[2])
print("{} {}".format(result[2], result[1]))

def rearrange_name(name):
    result = re.search(r'^(\w*), (\w*)$', name)
    if result is None:
        return name
    return "{} {}".format(result[2], result[1])

print(rearrange_name('Ritchie, Dennis'))


# repitition qualifiers
print(re.search(r'[a-zA-Z]{5}', 'a ghost'))
print(re.search(r'[a-zA-Z]{5}', 'a scary ghost appeared'))











