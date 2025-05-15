'''
print(5&2)
print(14<<3)
print(5<<1)
print(178<<13)

n = int(input())
if n & 1 ==0:
    print("even")
else:
    print("odd")


n = int(input())
if n | 1 == n:
    print("odd")
else:
    print("even")

if n % 2==0:
    if n ^ 1 == n+1:
        print("even")
else:
    print("odd")
 

n = int(input())
if bin(n^1)[-1] == '0':
    print("odd")
else:
    print("even")

#xor
def xorr(n):
    
    if n % 4 == 1:
        return 1
    elif n % 4 == 2:
        return n+1
    elif n % 4 == 3:
        return 0
    else:
        return n

m,n = map(int,input().split())
res = xorr(n) ^  xorr(m - 1)
print(res)


#print yes of input is in power of 2
#complexity = O(1)
n = int(input())
if n & n - 1 == 0:
    print("yes")
else:
    print("no")

#COMPLEXITY=LOGN
n = int(input())
i = 0
while 1:
    if (2**i == n):
        print("yes")
        break
    if (n < 2**i):
        print("no")
        break
    i = i + 1


#complexity big(n/2)
#sliding window
listt = [2,2,4,4,6,6,7,7,8,8]
n = len(listt)

for i in range(0,n-1,2):
    if listt[i] == listt[i+1]:
        i = i+2
    else:
        print(listt[i])
        break
else:
    print(listt[-1])

a = [1,2,3,2,3,4,5,6,7,8,9]
maxx = 1
hmaxx=1
for i in range(len(a)-1):
    if a[i]-a[i+1] == -1:
        maxx+=1
    else:
        hmaxx=max(hmaxx,maxx)
        maxx = 1
hmaxx =  max(hmaxx,maxx)
print(hmaxx)
'''
a='abbacbababc'
#a=[2,2,2,2,3,3,3,4,4,4,5,5,6,6,7,7,8,8]
maxx = 1
listt=[]
for i in range(len(a)-1):
    if a[i] == a[i+1]:
        maxx+=1
    else:
        listt.append(a[i])
        listt.append(str(maxx))
        maxx=1
listt.append(a[i+1])
listt.append(str(maxx))
#print(listt)
print("".join(listt))

        
        
        
        
    

        



























