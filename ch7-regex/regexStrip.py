#! python3
# regexStrip.py - A regex version of the strip() python method.

import re

def strip(text, char='\s'):
    stripRegex = re.compile(r'^' + '(' + char + '+)(\w+)(' + char + '+)')
    text = stripRegex.search(text)
    print(text.group(2))

strip('   dhkjfhdsf3ffdsfkf      ')
strip('-------fddsfdsafdasfdasffsdfs------', '-')

