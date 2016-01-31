'''
Created on Jan 31, 2016

@author: xiaobai
'''
def getfactors(num):
    factors = [1]
    for i in range(2,num+1):
        if not num%i:
            factors.append(i)
    return factors

#testCase
# print(getfactors(100))
