#! python3
# inputValidation.py - Simple collatz sequence function with try/except blocks.  

def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 12

while True:
    try:
        number = int(input('Enter a number to use in the collaz function, or enter "CTRL + C" to quit: '))
        print('Result: ' + str(collatz(number)))
    except ValueError:
        print('Invalid input, please enter a number.')
    