#! python3
# pdfPasswordBreaker.py - Tries to guess the password to a PDF by going through a list of words 
# provided in a txt file. If successful, prints out the password.
#
# NOTES: Run from command line, and provide the following arguments:
#        1. The filename/path for the txt file containing a list of words (one word per line) to try as a password.
#        2. The filename/path for the encrypted PDF you want try brute-forcing the password to.
#        This program assumes the words in the txt file are all uppercase.

import PyPDF2, sys

dictionaryText = sys.argv[1]
encryptedPdf = sys.argv[2]

pdfReader = PyPDF2.PdfFileReader(open(encryptedPdf, 'rb'))

f = open(dictionaryText)
words = f.readlines()
words = [word.rstrip() for word in words] # Remove the newline character at the end of each word.
f.close()

for word in words:
    print(word)
    if pdfReader.decrypt(word) == 1: # Try the word (uppercase, as written in the txt file) as a password.
        print('The password is: ' + '\'' + word + '\'')
        sys.exit()
    if pdfReader.decrypt(word.lower()) == 1: # Try the lowercase version of the word as a password.
        print('The password is ' + '\'' + word.lower() + '\'')
        sys.exit()

print('None of the words are the password.')