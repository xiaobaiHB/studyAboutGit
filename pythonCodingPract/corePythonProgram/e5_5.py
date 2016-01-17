'''
Created on Jan 17, 2016

@author: xiaobai
'''
print "auto dev dollar"

kindOfDollar = [0.25,0.1,0.05,0.01]

#TODO:how to judge input value is legal
howMoney = input('type input how much money you have:\n$')

print "$%s can dev into"%(howMoney)

for subK in kindOfDollar:
    print "%d of %d cent"%(howMoney/subK,subK*100)
    howMoney %= subK