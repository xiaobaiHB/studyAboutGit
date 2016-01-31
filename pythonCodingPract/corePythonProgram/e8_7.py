'''
Created on Jan 31, 2016

@author: xiaobai
'''

import e8_5

def isPerfect(num):
    if num < 1:
        return 0
    factors = e8_5.getfactors(num)
    factors.remove(num)
    sumx = 0
    for x in factors:
        sumx += x
    if sumx == num:
#         print "%d:%s"%(num,str(factors))
        return 1
    else:
        return 0
    
    
#TestCase
print [x for x in range(1000) if isPerfect(x)]