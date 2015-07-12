pyg = "ay" # saves pig latin suffix as a variable

original = raw_input("Enter text to translate: ")
original = original.split(" ") # transforms user input into list of words
new_text = []

consonants = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z', 'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

if len(original) > 0: # moves on if the user has entered text   
    for word in original:
    	orig_word = word
    	first = orig_word[0] 
    	second = orig_word[1]

#		LEFT OFF HERE 
#		if 

    	if first.isupper() == True: # transfers uppercase from first to second letter
    		first = first.lower()
    		second = second.upper()
    		    	
    	if word[-1].isalnum() == False: #for words that end in punctuation
    		punc = word[-1]
    		new_word = second + orig_word[2:-1] + first + pyg + punc # translates word into pig latin
    		new_text.append(new_word)

    	else:
    		new_word = second + orig_word[2:] + first + pyg # translates word into pig latin
    		new_text.append(new_word)
    		
    print "Your text in Pig Latin: " + " ".join(new_text)

else:
    print "You did not enter any text."
    
# modifications to make:
# 1. preserve punctuation for each word - DONE
# 2. if the word begins with a capital letter, so should the translated word - DONE
# 3. if the word contains no consonants, append "yay" instead of "ay"
# 4. program continuously takes more input
# see http://openbookproject.net/pybiblio/practice/wilson/piglatin.php