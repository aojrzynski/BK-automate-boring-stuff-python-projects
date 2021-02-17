#! python3
# fantasy_game_inventory2.py - Adds items from a list into a dictionary.

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby', 'emerald', 'emerald', 'sapphire']

def displayInventory(inventory):
    print('Inventory:')
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total += v
    print('Total Items: ' + str(item_total))

def addToInventory(inventory, added_items):
    for loot in dragonLoot:
        if loot not in inv:
            inv[loot] = 1
        else:
            inv[loot] += 1

addToInventory(inv, dragonLoot)
displayInventory(inv)