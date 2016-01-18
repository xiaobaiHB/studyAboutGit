'''
Created on Jan 18, 2016

@author: xiaobai
'''
bit10 = ('zero','one','two','three','four','five','six','seven','eight','nine','ten',
         'eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen')
bitx0 = ('','','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety')

# print "Translator of Arabic number"
# num = input("type what num you want to translate(between 0 to 1000):\n")
def transNum(num):
    if num/100:
        if num%100:
            print bit10[num/100],'hundred and',
            num%=100
        else:
            print bit10[num/100],'hundred'
            return
    if num>=20:
        if num%10:
            print '%s-%s'%(bitx0[num/10],bit10[num%10])
        else:
            print bitx0[num/10];
    else:
        print bit10[num]

#test module
for i in range(1000):
    transNum(i)