#! python3
# strongPasswordCheck.py - Uses regular expressions to make sure the password string it is passed is strong.

import re

hasLowerCaseLetter = re.compile(r'[A-Z]') 
hasUpperCaseLetter = re.compile(r'[a-z]')
hasDigit = re.compile(r'[0-9]')
isEightCharsLong = re.compile(r'\w{8,}')

def passwordStrenghCheck(password):
    if hasLowerCaseLetter.search(password) != None and hasUpperCaseLetter.search(password) != None and hasDigit.search(password) != None and isEightCharsLong.search(password) != None:
        print('Password is secure.')
    else:
        print('Password is not secure.')

passwordStrenghCheck('HjfurhHkf3jch0')
passwordStrenghCheck('fnfhsdfjhdshkfks')
passwordStrenghCheck('fsnkjfhsdkjfhasdkjfsd223')
passwordStrenghCheck('AHKHASKHFKJSAHKHS343')
passwordStrenghCheck('HFKJSDHFKhfkjhfjkds')
passwordStrenghCheck('aH8')

    