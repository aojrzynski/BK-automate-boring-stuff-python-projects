#! python3
# coinFlipStreak.py - Finds out how often a streak of six heads or a streak of six tails comes up in a 
# randomly generated list of heads and tails.

import random

numberOfStreaks = 0
for experimentNumber in range(10000):
    # Simulate 100 coin flips:
    coinFlips = []
    for i in range(100):
        throw = random.randint(0, 1)
        if throw == 0:
            coinFlips.append('T')
        else:
            coinFlips.append('H')

    # Check for streaks:
    streak = 6
    for j in range(len(coinFlips)):
        if streak == 6:
            numberOfStreaks += 1
        if j < 99 and coinFlips[j] == coinFlips[j+1]:
            streak += 1
        else:
            streak = 0

print("Chance of streak: %s%%" % (numberOfStreaks / 100))