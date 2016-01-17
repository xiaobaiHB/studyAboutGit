'''
Created on Jan 17, 2016

@author: xiaobai
'''
def strip(str):
    b = 0
    a = str.__len__()-1
    while str[b]== ' ':
        b+=1
        if b >= a:#avoid over index
            break
    while str[a]== ' ':
        a-=1
        if a <= b:
            break
    return str[b:a+1]#a to the end so plus one index
