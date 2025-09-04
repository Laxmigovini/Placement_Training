#find the floor of the square root of number
'''
n = 38
for i in range(1,n//2):
    if i*i>=n:
        print(i-1)
        break
    elif i*i>n:
        print(i-1)
        break

n = int(input())
l,r = 1,n//2
while l<=r:
    m = (l+r)//2
    if m*m == n:
        print(m)
        break
    if m*m>n:
        r = m-1
    elif m*m<n:
        l = m+1
print(r)#here asked floor so print r.

arr = [18,20,25,30,32,5,8,10,12,13]
l,r = 0,len(arr)-1
while l<r:
    m = (l+r)//2
    if arr[m]>arr[r]:
        l = m+1
    else:
        r = m
        
print(arr[l])

arr = [1,2,3,4,3,2,6,7,5,3,2,8,6,5,4,9,3,1]
l,r = 0,len(arr)-1
while l<r:
    m = (l+r)//2
    if (m == 0  or arr[m]>arr[m-1] and m == r or arr[m]>arr[m+1]):
        print(arr[m])
        break
    if arr[m]<arr[m+1] :
        l = m+1
    
    else:
        r = m-1
        


#koko eating banana
import math
arr = [3,6,7,11]
h = 8
k = 4
s = 0
for i in arr:
    s = s+ math.ceil(i/k)
if s == h:
    print("yes")
else:
    print("no")

#koko
import math
arr = [3,6,7,11]
h =8
k = 4
s = 0
while arr:
    s = 0
    for i in arr:
        if s>h:
            k = k + 1
            break
    else:
        print(k)
        break


#aggressive cows
a = [1,2,5,7,10,12]
mi = 5
while (1):
    cows = 3
    c1 = a[0]
    cows = cows-1
    for i in a:
        if i - c1 >= mi:
            c1 = i
            cows = cows-1
    if (cows <= 0):
        #print(mi)
        mi+=1 
    else:
        break
print(mi-1)
'''

def aggressiveCows(stalls, k):
    mi = 5
    while (1):
        c1 = stalls[0]
        k = k-1
        for i in stalls:
            if i - c1 >= mi:
                c1 = i
                k = k-1
        if k >= 0:
            mi+=1
    return (mi-1)
stalls = list(map(int,input().split()))
k = int(input())
print(aggressiveCows(stalls,k))
    
        

























    
        
     
    
