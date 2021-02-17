#! python3
# regexSearch.py - Opens all .txt files in a folder and searches for any line that matches a user-supplied regular expression.

import glob, re
from pathlib import Path

txtFiles = glob.glob('*.txt')

results = []
for txtFile in txtFiles:
    currentFile = open(txtFile)
    content = currentFile.read()
    currentFile.close()

    check = re.search(r'BLAAH', content)
    #check = userRegex.match(content)
    if check != None:
        results.append(txtFile)
print(results)



