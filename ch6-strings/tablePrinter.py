#! python3
# tablePrinter.py - Takes a list of lists of strings and displays it in a well-organized table with each column right-justified.

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

result = []

for innerList in range(4):
    text = []
    for outerList in range(3):
        text.append(tableData[outerList][innerList])
    result.append(text)

print(result)

for innerList in range(len(result)):
    for word in result[innerList]:
        print(word.ljust(10), end='')
    print()

        
        