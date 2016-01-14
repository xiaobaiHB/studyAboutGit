'''
Created on Jan 14, 2016

@author: xiaobai
'''
print "leap year judge app"

year = input('which year need judge:')

if (not(year % 4) and (year % 100)or(not(year % 4) and not(year % 100))):
    print '%d is leap year.'%year
else:
    print "%d isn't leap year."%year
