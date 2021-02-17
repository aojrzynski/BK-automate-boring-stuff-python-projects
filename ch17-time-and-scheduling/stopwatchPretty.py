#! python3
# stopwatchPretty.py - A simple stopwatch program, with slightly styled print output. Each print statement is copied to clipboard.

import time, pyperclip

# Display the program's instructions.
print('Press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch. Press CTRL-C to quit.')
input() # Press ENTER to begin.
print('Started')
startTime = time.time() # Get the first lap's start time.
lastTime = startTime
lapNum = 1

# Start tracking the lap times.
try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)

        lapSummary = 'Lap #%s: %s (%s)' % (str(lapNum).rjust(2), str(totalTime).rjust(5), str(lapTime).rjust(5)) # Create the string to be printed.
        print(lapSummary, end='') # Print the string.
        pyperclip.copy(lapSummary) # Copy the string to the clipboard.
        
        lapNum += 1
        lastTime = time.time() # Reset the last lap time.
except KeyboardInterrupt:
    # Handle the CTRL-C exception to keep its error message from displaying
    print('\nDone.')