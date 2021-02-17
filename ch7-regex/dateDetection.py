#! python3
# dateDetection.py - Detect dates in the DD/MM/YYYY format from text in the clipboard.

import pyperclip, re

dateRegex = re.compile(r'\d{2}/\d{2}/\d{4}')
text = str(pyperclip.paste())
matches = dateRegex.findall(text)

for date in matches:
    day = int(date[:2])
    month = int(date[3:5])
    year = int(date[6:])
    
    if month == 4 or month == 6 or month == 9 or month == 11:
        if day > 30:
            matches.remove(date)
    elif month == 2:
        if day > 28:
            matches.remove(date)
    elif day > 31:
        matches.remove(date)

    if month > 12:
        matches.remove(date)

print(matches)