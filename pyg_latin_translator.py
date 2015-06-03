# Translates one word into Pig Latin

pyg = "ay" # saves pig latin suffix as a variable

original = raw_input("Enter a word:") # asks user to input word

if len(original) > 0 and original.isalpha(): # moves on if the user's input was a string of letters only
    word = original.lower() # makes word input lowercase
    first = word[0] 
    new_word = word[1:] + first + pyg # translates
    print new_word
else:
    print "You did not enter a word."
