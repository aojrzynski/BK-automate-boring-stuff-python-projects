#! python3
# collatzSequence.py - Simple collatz sequence function.  

def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 12

while True:
    number = int(input('Enter a number to use in the collaz function, or enter "CTRL + C" to quit: '))
    print('Result: ' + str(collatz(number)))