# Given a list of filenames, we want to rename all the files with the
# extension hpp to the extension h by generating a list of tuples of
# the form (old_name, new_name).

# That is, given the following list of filenames
# filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# complete the starter code to generate the following newfilenames list of tuples
# newfilenames = [('program.c', 'program.c'), ('stdio.hpp', 'stdio.h'),
# ('sample.hpp', 'sample.h'), ('a.out', 'a.out'), ('math.hpp', 'math.h'), ('hpp.out', 'hpp.out')]

filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
newfilenames = []
for file in filenames:
    words = file.split(".")
    #print(words)
    if words[1] == "hpp":
        temp_list = []
        temp_list.append(words[0])
        new_file = words[0] + words[1]
        temp_list.append(new_file)
        newfilenames.append( tuple(temp_list) )
        #print(newfilenames)
    else:
        new_list = []
        new_list.append(words)
        new_list.append(words)
        newfilenames.append( tuple(new_list) )

    #print(words)


print (newfilenames)
# Should be [('program.c', 'program.c'), ('stdio.hpp', 'stdio.h'),
# ('sample.hpp', 'sample.h'), ('a.out', 'a.out'), ('math.hpp', 'math.h'),
# ('hpp.out', 'hpp.out')]