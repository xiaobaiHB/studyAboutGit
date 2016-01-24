'''
Created on Jan 20, 2016

@author: xiaobai
'''
from numbers import Real
def atoc(strC):
    real = 0
    imag = 0
    if 'j' in strC:
        poxj = strC.index('j')
        if poxj+1 == len(strC):
            if not strC[poxj-1] in '+-':
                for i in range(poxj,-1,-1):
                    if strC[i] in '+-' and strC[i-1].isdigit():
                        real = strC[:i]
                        imag = strC[i:poxj]
                        break
                    if i == 0:
                        imag = strC[:poxj]
            else:
                real = strC[:poxj-1]
                imag = strC[poxj-1]+'1'
        else:
            real = strC[poxj+1:]
            imag = strC[:poxj]
    else:
        real = strC
#    judge if real/imag is not float
#     print real
#     print imag
    return complex(float(real),float(imag))
    
# test func atoc()
print atoc('-1.23e+4-5.67j')