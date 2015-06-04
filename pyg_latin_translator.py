# Translates multiple words into Pig Latin

pyg = "ay" # saves pig latin suffix as a variable

original = raw_input("Enter text to translate: ")
original = original.split(" ")
new_text = []

if len(original) > 0: # moves on if the user has entered text   
    for i in original:
    	word = i.lower() # makes word input lowercase
    	first = word[0] 
    	new_word = word[1:] + first + pyg # translates word into pig latin
    	new_text.append(new_word)
    print "Your text in Pig Latin: " + " ".join(new_text)
else:
    print "You did not enter any text."
