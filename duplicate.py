'''
listt = [9,3, 4, 5,3,3, 5, 6, 7,7, 8,]
map1 = dict()
for i in listt:
    if i in map1:
        map1[i]+=1
    else:
        map1[i] = 1

list2 = list(map1)
print(list2)

a=7
b=0
a=a-2
b=b+1+1
b=b-1
c =a^b
print(c)
    

def sum(n):
    if n == 0:
        return 0
    return n + sum(n - 1)
n = int(input())
print(sum(n))

'''
n = int(input())
s= 0
for i in range( 1, n+1):
    s = s + i
print(s)    #BigO(n)

lst = list(map(int,input().split()))
s = 0
for i in range(1,len(lst),2):
    #if i % 2==0:
    s+=lst[i]
print(s)
        















