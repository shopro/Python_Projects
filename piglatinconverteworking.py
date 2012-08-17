original = raw_input('Enter a word:')
pyg = 'ay'
word = original.lower()
first = word[0]
if len(original) != 0 and original.isalpha():
  if first in ("a","e","i","o","u"):
    print "vowel"
    new_word = str(word) + str(pyg)
    print new_word
  else: 
    print "consonant"
    first_letter = word[0:1]
    word_1 = word[1:len(word)]
    new_word = str(word_1) + str(first_letter) + str(pyg)
    print new_word
else:
    print 'Invalid'
