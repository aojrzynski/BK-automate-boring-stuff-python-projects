#! python3
# fillInGaps.py - Finds all files with a given prefix, locates any gaps in the numbering and renames files to close that gap. 

import os, re, shutil

os.chdir(r'/example/path')
path = os.getcwd()

# Regex to use in identifying files.
prefix_regex = re.compile(r'(example)(\d{,3})')

i = 1
for file in os.listdir():
    mo = prefix_regex.search(file)
    if mo:
        old_name = os.path.abspath(file)
        new_suffix = mo.group(1) + str(i).zfill(3) + '.txt'
        new_name = os.path.join(path, new_suffix)
        i += 1
        print('Renaming: %s to %s' % (old_name, new_name))
        shutil.move(old_name, new_name)