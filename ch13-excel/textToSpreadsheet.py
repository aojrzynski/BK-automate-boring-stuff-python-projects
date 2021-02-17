#! python3
# textToSpreadsheet.py - Reads in the contents of several text files and and inserts 
# those contents into a spreadsheet, with one line of text per row.
#
# NOTES: Run this program via command line and provide filenames as arguments. The files should be in the same location as this program.

import openpyxl, sys

# Create a list with all the filenames (provided via command line).
try:
    textFiles = [arg for arg in sys.argv[1:]]
except:
    print('Please provide filenames as arguments.')
    sys.exit()

wb = openpyxl.Workbook()
ws = wb.active

# Loop through each filename in 'textFiles', open each file, read the lines and store them in a 'lines' variable.
column = 1
for textFile in textFiles:
    try:
        f = open(textFile, 'r')
    except:
        print('This file does not exist. Skipping to the next one.')
        continue
    lines = f.readlines()
    f.close()

    # Loop through each line stored in 'lines' and add each line to the workbook object.
    row = 1
    for line in lines:
        ws.cell(row=row, column=column, value=line)
        row += 1

    column += 1

wb.save('textToSpreadsheetResult.xlsx')
