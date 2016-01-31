#code GBK
'''
Created on Jan 31, 2016

@author: xiaobai
'''
def listASCII(begin,end):
    print "DEC       BIN       OCT       HEX       ASCII"
    print '-'*50
    for i in range(begin,end+1):
        print "%-10d%-10s%-10o%-10x%-10c"%(i,bin(i),i,i,i) 
        
        
listASCII(26, 41)