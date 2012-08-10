original = raw_input('Enter a word:')
pyg = 'ay'
word = original.lower()
first = word[0]
# Yes, the isalpha() here checks that it's alphabetic, but then say
# it's numbers -- the error printed out is "empty", which is misleading.
if len(original) != 0 and original.isalpha():
	if first==("a","e","i","o","u")
		print "vowel"
		new_word = word + pyg
		print new_word
	else: 
		print "consonant"
		first_letter = word[0:1]
		word_1 = word[1:len(word)]
		new_word = word_1 + first_letter + pyg
		print new_word
else:
	print 'empty'
