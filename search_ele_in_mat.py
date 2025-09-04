'''
a = [2,8,7],[9,5,7],[1,3,4]
target = 2
for i in range(len(a)):
    flag = 0
    for j in range(len(a)):
        if a[i][j]==target:
            print("found")
            flag = 1
            break
    if flag == 1:
        break
    
else:
    print("not found")
    

a = [[2,3,5,7],[9,15,20,22],[23,26,35,37],[38,39,42,43]]
arr = a[0]
l,r = 0,len(arr)-1
target = 3

def binary_search(arr,target):
    l,r = 0,len(arr)-1
    while l<=r:
        m = (l+r)//2
        if arr[m]==target:
            return True
            
           
        elif arr[m]<target:
            l = m+1
        else:
            r = m-1
    
a = [[2,3,5,7],[9,15,20,22],[23,26,35,37],[38,39,42,43]]
target = 15
for i in range(len(a)):
    if binary_search(a[i],target):
        print("ele found")
        break
    

a = [[2,3,5,7],[9,15,20,22],[23,26,35,37],[38,39,42,43]]
target = 7
n = 4
left,right=0,(n*n) - 1

while left <= right:
    mid=(left+right)//2
    row,col=mid // n, mid % n
    if a[row][col] == target:
        print("Element found")
        break
    elif a[row][col]<target:
        left=mid+1
    else:
        right=mid-1
else:
    print("Not found")




#capacity of ship packages
wei = [1,2,3,4,5,6,7,8,9,10]
capac = 12
d = 1
s = 0
for i in wei:
        if s+i > capac:
            d+=1
            s = i
        else:
            s+=i

    
print(d)
#or
wei = [1,2,3,4,5,6,7,8,9,10]
capac = 15
d = 0
s = 0
i = 0

while i < len(wei):
    s += wei[i]
    if s > capac:
        d += 1
        s = 0
    else:
        i += 1


if s > 0:
    d += 1

print(d)

#2sum
a = [2,7,11 ,15]
target = 22
i,j = 0,len(a)-1
while i<j:
    if a[i]+a[j] == target:
        print(a[i],a[j])
        break
    elif a[i]+a[j]<target:
        i+=1
    else:
        j-=1
        




#capacity of ship packages
wei = [1,2,3,4,5,6,7,8,9,10]
capac = 15
d = 1
s = 0
for i in wei:
        if s+i > capac:
            d+=1
            s = i
        else:
            s+=i

    
print(d)
'''


l1 = [2,4,3]
l2 = [5,6,4]
#Output: [7,0,8]
i,j = 0,0
res = []
carry = 0
while i<len(l1) or j<len(l2) or carry:
    val1 = l1[i] if i<len(l1) else 0
    val2 = l2[j] if j<len(l2) else 0
    total = val1+val2+carry
    res.append(total%10)
    carry = total//10
    if i<len(l1):
        i+=1
    if j<len(l2):
        j+=1
print(res)



















