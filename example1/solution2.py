#Eg. 1 -- Common Design Mistakes
#Program Goal: Print a list of words delimited by commas

#Solution 2:
list_of_words = ["hello", "yes", "goodbye", "last"]
to_print = ""

for i in range(len(list_of_words)):
    to_print += list_of_words[i]
    if i != len(list_of_words) - 1:
        to_print += ","
        
print(to_print)