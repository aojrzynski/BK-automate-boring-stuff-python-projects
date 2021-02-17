#! python3
# spreadsheetToText.py - Writes the contents of a column from a specified spreadsheet into 
# a text file. Each row of a column is one line, each column is one file.
#
# NOTES: Run the program from command line and provide the spreadsheet filename as an argument.

import openpyxl, sys

# Create a workbook item from the spreadsheet provided by command line. 
try:
    wb = openpyxl.load_workbook(sys.argv[1])
except:
    print('That filename cannot be found or is not a spreadsheet. Please provide a valid filename.')
    sys.exit()
ws = wb.active

# Go through each column in the workbook. For each column, create a new text 
# file and write the values from the column's rows into it (each cell is a new line).
count = 1
for column in ws.iter_cols():
    f = open('text' + str(count) + '.txt', 'w') 
    count += 1

    for cell in column:
        if cell.value == None:
            continue
        f.write(cell.value)
    
    f.close()


