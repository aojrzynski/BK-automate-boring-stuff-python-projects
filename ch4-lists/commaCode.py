#! python3
# commaCode.py - Takes a list value as an argument and returns a string with all the items 
# separated by a comma and a space, with "and" inserted before the last item.

spam = ['apples', 'bananas', 'tofu', 'cats']

def commeCode(listValue):
    result = ''
    for item in listValue:
        if item == listValue[-1]:
            result += ("and " + str(item))
        else:
            result += (item + ", ")
    return result

print(commeCode(spam))