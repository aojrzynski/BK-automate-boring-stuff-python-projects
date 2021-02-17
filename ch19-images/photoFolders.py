#! python3
# photoFolders.py - Goes through every folder on your hard drive and finds potential photo folders.
#
# NOTES: Enter your computer's root path in os.walk. For example, 'C:\\' on Windows.

import os
from PIL import Image

for foldername, subfolders, filenames in os.walk('.'):
    numPhotoFiles = 0
    numNonPhotoFiles = 0
    for filename in filenames:
        # Check if the file extension isn't .png or .jpg
        if not filename.lower().endswith(('.png', '.jpg')):
            numNonPhotoFiles += 1
            continue

        # Open image using Pillow.
        im = Image.open(os.path.join(foldername, filename))
        width, height = im.size
        # Check if width and height are larger than 500.
        if width > 500 and height > 500:
            #print(foldername)
            # Image is large enough to be considered a photo.
            numPhotoFiles += 1
        else:
            # Image is too small to be a photo.
            numNonPhotoFiles += 1
    
    # If more than half the files were photos, print absolute path of the folder.
    if numPhotoFiles > numNonPhotoFiles:
        print(os.path.abspath(foldername) + ': %s photos, %s non-photos.' % (numPhotoFiles, numNonPhotoFiles))