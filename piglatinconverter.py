original = raw_input('Enter a word:')
pyg = 'ay'
word = original.lower()
first = word[0]
if len(original) != 0 and original.isalpha():
	# Rewrite next line using "if BLAH in (A, B, C)" syntax
	if first=='a' or first=='o' or first=='i' or first=='e' or first=='u':
		print "vowel"
                # Do this without converting strings to strings:
		new_word = str(word) + str(pyg)
		print new_word
	else: 
		print "consonant"
		first_letter = word[0:1]
		word_1 = word[1:len(word)]
                # Do this without converting strings to strings:
		new_word = str(word_1) + str(first_letter) + str(pyg)
		print new_word
else:
	print 'empty'

# Are you testing enough cases?  What if someone passes "123"?  That's
# not empty, but it's not pig-latinable either.  Expand the error
# condition handling to cover every conceivable case.

# Other than the above, code looks good, btw!
