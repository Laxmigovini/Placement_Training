
'''def qwer():
    print("hi")
    asd()
def asd():
    print("hry")
    qwer()
    print(2)
def zxc():
    print("hello")


qwer()
print(3)
asd()
'''

'''
import sys
sys.setrecursionlimit(3000)
#by setting the limit for recursive calls recursion depth can be increased

def qwer(x):
    if x == 6:
        return 200
    print("hi",x)
    b = qwer(x+1)
    print("hi",x)#here it prints in reverse order because it has additional path.
    #it notes down the preveious order. it stores the order. it has storage feature
    #sothat it doesnot reach infinite
    return b + x # 200+5 , 200+4,..... 200+1= 215
b = qwer(1)
print(b)




def qwer(x):
    if x == 4:
        return 1
    return x + qwer(x+1)
b = qwer(1)
print(b)





def qwer(x):
    if x == 1:
        return 1
    if x==2:
        return 1
    return qwer(x-1)+qwer(x-2)
for i in range(1,14):
    b = qwer(i)
    print(b)




def even_sum(x,i):
    if len(x)==i:
        return 0
    if x[i]%2 == 0:
        return x[i] + even_sum(x,i+1)
    else:
        return even_sum(x,i+1)

a = [2,5,6,7,2,1,4,3,6]
print(even_sum(a,0))

def even_sum(x):
    if len(x)==0:
        return 0
    if x[0]% 2 == 0:
        print(len(x))
        return x[0] + even_sum(x[1:])
    #else:
       # return even_sum(x[1:])
    return even_sum(x[1:])

a = [2,5,6,7,2,1,4,3,6]
print(even_sum(a))



def reverse(n, re = 0):
    if n == 0:
        return re
    return reverse(n//10, re*10 + n%10)
n = int(input())
print(reverse(n))




def is_prime(n,i = 2):
    if n <=1:
        return False
    if n == 2 or n == 3:
        return True
    if n % i == 0:
        return False
    if i * i > n: #or i == (n/2)+1:
        return True
    return is_prime(n,i+1)
def iteration(n,count=0):
    if len(n)==0:
        return count
    if is_prime(n[0]):
        return iteration(n[1:],count+1)
    else:
        return iteration(n[1:],count)
    
    
n = [2,3,5,7,8]
print(iteration(n))



def find(n):
    i = 3
    j = 5
    temp = 1
    while 1:
        n -= i
        if n == 1:
            temp = 1
            return True
        elif n < 1:
            return False
    return False
n = int(input())
print(find(n))
   

def qwer(n,i,j, c = 0):
    if n == 1:
        return True,c
    if n < 1:
        return False
    return qwer(n-i,i,j,c+1) or qwer(n-j,i,j,c+1)

print(qwer(9,3,5))
'''


def bfs(n,i,j):
    visited = set()
    q = []
    q.append(n)
    visited.add(n)
    while 1:
        q.pop[0]
        






















    
    














    














