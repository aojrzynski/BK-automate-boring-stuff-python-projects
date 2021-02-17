#! python3
# sandwichMakes.py - Program that asks users for their sandwich preferences as if ordering a sandwich, then prints the results/order.

import pyinputplus as pyim

breadType = pyim.inputMenu(['Wheat', 'White', 'Sourdough'], prompt='What kind of bread?')
proteinType = pyim.inputMenu(['Chicken', 'Turkey', 'Ham', 'Tofu'], prompt='What kind of protein?')
cheese = pyim.inputYesNo(prompt='Do you want cheese?')
if cheese == 'yes':
    cheeseType = pyim.inputMenu(['Cheddar', 'Swiss', 'Mozzarella'], prompt='What kind of cheese?')
extras =  pyim.inputYesNo(prompt='Do you want mayo, mustard, lettuce or tomato?')
howManySandwiches = pyim.inputInt(prompt='How many sandwiches do you want?', min=1)

print('Your order details are below:')
print('Bread type: ' + breadType)
print('Protein type: ' + proteinType)
if cheese == 'yes':
    print('Cheese type: ' + cheeseType)
if extras == 'yes':
    print('All the extras on top.')
print('Ordered %s sandwiches' % (howManySandwiches))
