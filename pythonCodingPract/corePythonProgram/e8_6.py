'''
Created on Jan 31, 2016

@author: xiaobai
'''
import e8_4
import e8_5

def devFactor(num):
    factors = e8_5.getfactors(num)
    if len(factors)>2:
        for i in factors:
            if e8_4.isprime(i) and i > 1:
                return [i]+devFactor(num/i) #[i].append(devFactor(num/i)) return None because append() did not new one list
    else:
        return [num]
        
#testCase
print devFactor(20)