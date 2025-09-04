'''def binary(n,s=""):
    if len(s) == n:
        print(s)
        return
    binary(n,s+'1')
    binary(n,s+'0')
binary(4)
'''
import math
def allbinary(a,n,s=''):
    if len(s) == n:
        if int(s,2) <= a:
            print(s)
        return 
    allbinary(a,n,s+'1')
    allbinary(a,n,s+'0')
a=10
n=int(math.log(a,2))+1
allbinary(a,n)