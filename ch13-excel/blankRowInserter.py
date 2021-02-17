#! python3
# blankRowInserter.py - Takes three arguments from the command line (a number N, a number M and a filename), 
# then starting at row N in the filename, inserts M blank rows.
#
# NOTES: Run this program from the command line, and include three arguments:
#        1. The row number you want to start inserting blank rows at.
#        2. How many blank rows you want to insert.
#        3. Filename of the excel file you want to perform this operation on (easiest if the file is in the same location as this program). 

import openpyxl, sys

# Assign the first two arguments to variables. If the arguments aren't valid integers, run the exception.
try:    
    n = int(sys.argv[1])
    m = int(sys.argv[2])
except:
    print('Please make sure the first two arguments are numbers.')
    sys.exit()

# Create a workbook object from the provided filename. If this fails run the exception.
try:
    wb = openpyxl.load_workbook(filename=sys.argv[3])
except:
    print('Please provide a valid filename.')
    sys.exit()

ws = wb.active

# Insert the blank rows into the file.
for i in range(m):
    ws.insert_rows(n)
    n += 1

wb.save(sys.argv[3])


