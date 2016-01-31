'''
Created on Jan 31, 2016

@author: xiaobai
'''
def isprime(num):
    for i in range(2,num):
        if not num%i:
            return  False
    return True


#testCase
# print [x for x in range(1,100) if isprime(x)]