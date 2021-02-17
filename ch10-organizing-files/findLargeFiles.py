#! python3
# findLargeFiles.py - Uses os.walk to crawl through a specified location and print out all siles above the specified size.
# 
# NOTES: In the function call provide the following:
#   1. Location to use os.walk on.
#   2. Size threshhold for the files (any file larger than this will be printed in the terminal.)

import os

def findLargeFiles(folder, size):
    for foldername, subfolders, filenames in os.walk(folder):
        print(f'Looking through {foldername}...')
        for filename in filenames:
            filenamePath = os.path.join(foldername, filename)
            filenameSizeMB = round(os.path.getsize(filenamePath)/(1024*1024), 2)
            if filenameSizeMB > size:
                print(f'-----{filename}: {filenameSizeMB}')
    print('All done.')

findLargeFiles('/Users/aojrzyns/Documents', 100)
