#! python3
# selectiveCopy.py - Walks through a folder structure using os.walk, 
# copying all files with the specified extension to the specified destination.
# 
# NOTES: In the function call, provide the following:
#   1. The location the function should walk through.
#   2. The file extension you are looking for.
#   3. A location for the files to be copied to.

import shutil, os

def selectiveCopy(folder, extension, destination):
    for foldername, subfolders, filenames in os.walk(folder):
        print(f'Looking through {foldername} for files ending with {extension}')
        for filename in filenames:
            if filename.endswith(extension):
                shutil.copy(os.path.abspath(filename), destination)
                print(f'Copying {filename} to {destination}...')
    print('All done.')

selectiveCopy(os.getcwd(), '.txt', '/Users/aojrzyns/Documents/txtfiles')
