'''
Created on Jan 18, 2016

@author: xiaobai
'''

print "turn over between upper and lower case"

subS = raw_input('type what string you want to change:\n')
resS = ''
for subC in subS:
    if subC.isalpha():
        if subC.islower():
            resS += subC.upper()
        else:
            resS += subC.lower()
    else:
        resS += subC

print resS