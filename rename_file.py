# Author:           Sandro Aguilar


#The email_list function receives a dictionary, which contains domain
# names as keys, and a list of users as values. Fill in the blanks to
# generate a list that contains complete email addresses (e.g. diana.prince@gmail.com).
def email_list(domains):
    emails = []
    for key in domains:
        print(key)
        for user in users:
            print(user)
            emails.___
    return(emails)

print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))



# Let's create a function that turns text into pig latin: a simple text transformation
# that modifies each word moving the first character to the end and appending "ay" to
# the end. For example, python ends up as ythonpay.
def pig_latin(text):
    say = ""
    temp_list = []
    # Separate the text into words
    words = text.split()
    for word in words:
        # Create the pig latin word and add it to the list
        temp_word = word[1:] + word[0] + "ay"
        # Turn the list back into a phrase
        temp_list.append(temp_word)
        say = ' '.join(temp_list)
    return say          # added words

# print(pig_latin("hello how are you"))
# Should be "ellohay owhay reaay ouyay"
# print(pig_latin("programming in python is fun"))
# Should be "rogrammingpay niay ythonpay siay unfay"







# The permissions of a file in a Linux system are split into three sets of three
# permissions: read, write, and execute for the owner, group, and others. Each of
# the three values can be expressed as an octal number summing each permission, with
# 4 corresponding to read, 2 to write, and 1 to execute. Or it can be written with a
# string using the letters r, w, and x or - when the permission is not granted. Fo
# example: 640 is read/write for the owner, read for the group, and no permissions for
# the others; converted to a string, it would be: "rw-r-----" 755 is read/write/execute
# for the owner, and read/execute for group and others; converted to a string, it would
# be: "rwxr-xr-x" Fill in the blanks to make the code convert a permission in octal
# format into a string format.
def octal_to_string(octal):
    result = ""
    value_letters = [(4,"r"),(2,"w"),(1,"x")]
    # Iterate over each of the digits in octal
    for x in [int(n) for n in str(octal)]:
        # print(x)                # 7
        # print(octal)            # 755
        # Check for each of the permissions values
        for value, letter in value_letters:
            # print(value)        # 4
            # print(letter)       # r
            if x >= value:          # added 'x'
                result += letter       # added 'r'
                x -= value
            else:
                result += '-'
    return result

# print(octal_to_string(755)) # Should be rwx r-x r-x
# print(octal_to_string(644)) # Should be rw- r-- r--
# print(octal_to_string(750)) # Should be rwx r-x ---
# print(octal_to_string(600)) # Should be rw- --- ---


# Given a list of filenames, we want to rename all the files with the
# extension hpp to the extension h by generating a list of tuples of
# the form (old_name, new_name).

# That is, given the following list of filenames
# filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# complete the starter code to generate the following newfilenames list of tuples
# newfilenames = [('program.c', 'program.c'), ('stdio.hpp', 'stdio.h'),
# ('sample.hpp', 'sample.h'), ('a.out', 'a.out'), ('math.hpp', 'math.h'), ('hpp.out', 'hpp.out')]

# filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# newfilenames = []
# for file in filenames:
#     words = file.split(".")
#     #print(words)
#     if words[1] == "hpp":
#         temp_list = []
#         temp_list.append(file)
#         new_file = words[0] + "." + "h"
#         temp_list.append(new_file)
#         newfilenames.append( tuple(temp_list) )
#         #print(newfilenames)
#     else:
#         new_list = []
#         new_list.append(file)
#         new_list.append(file)
#         newfilenames.append( tuple(new_list) )

# print (newfilenames)
# Should be [('program.c', 'program.c'), ('stdio.hpp', 'stdio.h'),
# ('sample.hpp', 'sample.h'), ('a.out', 'a.out'), ('math.hpp', 'math.h'),
# ('hpp.out', 'hpp.out')]