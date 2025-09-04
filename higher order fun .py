x=lamda
a*10
print(x(10)) 
#filter Example: 
age = [21,34,12,15,22] 
def myfun(x): 
    if x<18: 
        return False 
    else: 
        return True 
adults = filter(myfun,age) 
for x in adults: 
    print(x) 
#map Example 
def myfun1(x): 
    return len(x) 
x = map(myfun1,('apple','ant','ass')) 
print(x) 
print(list(x)) 
def myfun2(a, b): 
    return a+b 
x = map(myfun2,('apple','ant','ass'),('red','black','yellow')) 
print(x) 
print(list(x)) 
#reduce Example: 
from functools import reduce 
def do_sum(x1,x2): 
    return x1+x2 
print(reduce(do_sum,[1,2,3,4,5]))
