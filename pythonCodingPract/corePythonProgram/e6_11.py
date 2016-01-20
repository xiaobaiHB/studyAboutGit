'''
Created on Jan 20, 2016

@author: xiaobai
'''
print "Dot-decimal notation translation"

strMAC = raw_input('type a Integer value and change into MAC:\n')
try:
    intMac = int(strMAC)
except (Exception):
    print "'%s' is not Integer(Illegal)"%strMAC
    intMac = 0
MAC = ''

for i in range(3,-1,-1):
    MAC += '%3d'%(intMac>>(i*8)&0xff)
    if i:
        MAC += '.'

print MAC