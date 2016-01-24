'''
Created on Jan 24, 2016

@author: xiaobai
'''
import random

print ">>Rochambeau<<"

roch = ['paper','rock','scissors']

def judgeRoch(selRoch):
    rules = ((0,1,-1),(-1,0,1),(1,-1,0))

    rndRoch = random.choice(roch)
    print 'PC show %s'%rndRoch
    return rules[roch.index(selRoch)][roch.index(rndRoch)]

#test judgeRoch
rounds = 0
while True:
    try:
        rounds = input("type how many times in a round:")
        if rounds%2:
            break
        else:
            print 'rules not illegal'
    except Exception:
        print 'input error'

res = 0
print 'p:paper;r:rock;s:scissors:'
while True:
    typeRoch = raw_input()
    if typeRoch == 'p':
        res += judgeRoch('paper')
    elif typeRoch == 'r':
        res += judgeRoch('rock')
    elif typeRoch == 's':
        res += judgeRoch('scissors')
    else:
        print 'input error'
    if abs(res)>rounds/2:
        if res > 0:
            print 'you win!'
        else:
            print 'you loss!'
        break
