#! python3
# excelToCsvConverter.py - Reads all the Excel files in the current working directory and outputs them as CSV files.
#
# NOTES: Run this program in the same directory as the Excel files you wish to target.

import csv, openpyxl, os

# Loop through each file.
for currentFile in os.listdir('.'): 
    if not currentFile.endswith('.xlsx'): # Skip non xslx files
        continue
    wb = openpyxl.load_workbook(currentFile)

    # Loop through each sheet of the workbook.
    for sheetName in wb.get_sheet_names(): 
        sheet = wb.get_sheet_by_name(sheetName)
        csvFilename = currentFile[:-5] + '_' + sheetName + '.csv' # Create the CSV filename from the Excel filename and sheet title.
        outputFile = open(csvFilename, 'w', newline='')
        outputWriter = csv.writer(outputFile)

        # Loop through each row in the sheet.
        for rowNum in range(1, sheet.max_row + 1):
            rowData = []
            # Loop through each column in the sheet.
            for colNum in range(1, sheet.max_column + 1):
                cellValue = (sheet.cell(row=rowNum, column=colNum).value)
                rowData.append(cellValue)
            outputWriter.writerow(rowData)

        outputFile.close()
    