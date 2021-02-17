#! python3
# madlibs.py - reads in text files and lets the user add their own text anywhere the word
# ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file.
#
# NOTES: Needs a story.txt file to be in the same location as this program.

import re
import pyinputplus as pyip
from pathlib import Path

# Open, save and print the content of the file.
storyFile = open('story.txt')
content = storyFile.read()
storyFile.close()
print('This is the text you can work with:')
print('"' + content + '"')

# Ask the user to replace strings within the file.
content = re.findall(r"[\w']+|[.,!?;]", content)
for i, word in enumerate(content):
    if word.lower() == 'adjective':
        content[i] = pyip.inputStr(prompt='Enter an adjective:')
    elif word.lower() == 'noun':
        content[i] = pyip.inputStr(prompt='Enter a noun:')
    elif word.lower() == 'adverb':
        content[i] = pyip.inputStr(prompt='Enter an adverb:')
    elif word.lower() == 'verb':
        content[i] = pyip.inputStr(prompt='Enter a verb:')

# Find the ends of sentances and modify the list so there is no space before a word and a dot.
# Example: 'Hello World .' is bad. 'Hello World.' is good.
pattern = re.compile(r'\w+\.')
for i in range(len(content) - 1):
    if i != len(content) - 1: 
        if pattern.match(content[i] + content[i + 1]):
            content[i] = content[i] + content[i + 1]
            content[i + 1] = '--$$**DELETE**$$--'
for i in range(len(content) - 1):
    if content[i] == '--$$**DELETE**$$--':
        del content[i]
content = ' '.join(content)


# Write the new string to the file and print.
storyFile = open('story.txt', 'w')
storyFile.write(content)
storyFile.close()
print('The result:')
print(content)

