'''
Created on Jan 14, 2016

@author: xiaobai
'''
res = input('type scroe:')
lv = 'F'

if res >= 90:
    lv = 'A'
elif res >= 80:
    lv = 'B'
elif res >= 70:
    lv = 'C'
elif res >= 60:
    lv = 'D'

print lv