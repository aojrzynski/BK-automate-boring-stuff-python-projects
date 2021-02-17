#! python3
# coinToss.py - A coin toss guessing game.

import random, logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')
logging.disable(logging.CRITICAL)

guess = ''
while guess.lower() not in ['heads', 'tails']:
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()

toss = random.choice(['heads', 'tails'])
logging.debug(toss + ' : ' + guess)
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')