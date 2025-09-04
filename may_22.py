'''
ip = [2,2,1,0,1,3,0]
res = 0
for i in range(len(ip)):
    
        
    if res < ip[i]:
        res = ip[i]
        res = res -1
    elif res>ip[i]:
        res-=1
if res == 0:
    print("not possible")
        
else:
    print("possible")

#lemonade change
ip = [5,10,5,10,10,20]
five = 0
ten = 0
n = len(ip)
t = True
for i in range(n):
    if ip[i] == 5:
        five+=1
    elif ip[i] == 10:
        ten +=1
        if  five>0:
            five-=1
        else:
            t = False
    elif ip[i] == 20:
        if five>=3:
            five-=3
        elif ten >=1 and five >=1:
            ten-=1
            five-=1
        else:
            t = False
if t == True:
    print("possible")
else:
    print("not possibe")

#shortest job first
ip = [4,3,7,1,6,2]
ip.sort()
s = 0
n = len(ip)
for i in range(len(ip)):
    s = s + ip[i]
res = s // n
print(res)
 
#cookies
ppl = [1,6,2,3,4,5]
bun = [4,2,3,1,1,2]

ppl.sort()
bun.sort()
bun2 = len(bun)
for i in range(len(ppl)):
    for j in range(len(bun)):
        if ppl[i]<=bun[j]:
            bun.remove(bun[j])
            break
            
print(bun2 - len(bun))



#jump game 2
nums = [2,3,1,1,4]
l,r = 0,0
jump = 0

while r<len(nums)-1:
    maxi = 0
    f = 0
    for i in range(l,r+1):
        if i +nums[i] > maxi:
            maxi = i + nums[i]
        if maxi>=len(nums):
            f = 1
            break
    l = r+1
    r = maxi
    jump = jump+1
    if f == 1:
        break
print(jump)
 '''
def binary_search(number,precision):
    l,r = 0,number//2
    res = 0
    while l<=r:
        m = (l+r)//2
        if m*m == number:
            res = m
            break
        elif m*m >number:
            r = m-1
            
        else:
            res = m
            l = m + 1
    increment = 0.1
    for _ in range(precision):
        while (res+increment) * (res+increment) <=number:
            res+=increment
        increment/=10
    return round(res,precision)
number = int(input())
precision = int(input())
print(binary_search(number,precision))
            





















        























        
        
        
