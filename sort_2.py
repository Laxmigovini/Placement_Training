'''ip1 = [2,4,5,8,9]
ip2 = [3,5, 6,9,11,12,13]


ip=[]
i,j = 0,0
while i<len(ip1) and j<len(ip2):
    if ip1[i]<ip2[j]:
        ip.append(ip1[i])
        i = i+1
    else:
        ip.append(ip2[j])
        j+=1
while j<len(ip2):
    ip.append(ip2[j])
    j+=1
while i<len(ip1):
    ip.append(ip1[i])
    i+=1
print(ip)



def mergesort(arr):
    if len(arr)<=1:
        return arr
    
    mid = len(arr)//2
    ip1 = mergesort(arr[:mid])
    ip2 = mergesort(arr[mid:])
    
    i,j = 0,0
    ip =[]
    while i<len(ip1) and j<len(ip2):
        if ip1[i]<ip2[j]:
            ip.append(ip1[i])
            i = i+1
        else:
            ip.append(ip2[j])
            j+=1
    while i<len(ip1):
        ip.append(ip1[i])
        i+=1
    while j<len(ip2):
        ip.append(ip2[j])
        j+=1
    
    return ip
   
arr = [3,5,6,1,2,3,87,5,4,3,2,9]
print(mergesort(arr))

def mergesort(l):
    if len(l) > 1:
        mid = len(l) // 2
        L = l[:mid]
        R = l[mid:]
        mergesort(L)
        mergesort(R)
        i,j,k = 0,0,0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:   
                l[k] = L[i]
                i = i + 1
            else:
                l[k] = R[j]
                j = j + 1
            k += 1

        while i < len(L):
            l[k] = L[i]
            k += 1
            i += 1

        while j < len(R):
            l[k] = R[j]
            k += 1
            j += 1

    return l    
    

l = [4,6,2,8,9,2,8,0,4,8,9,9,0,45,2,3]
l.sort()
print(l)
print(mergesort(l))


arr = [4,2,1,6,7,8,9,5,21,8,12,20,19]
freq = dict()
for i in arr:
    if i in freq:
        freq[i]+=1
    else:
        freq[i] = 1
n = max(arr)
bucket = []
k = 3
for _ in range(n):
    bucket.append([])
#print(bucket)
for keys,value in freq.items():
    bucket[keys-1].append(keys)
#print(bucket)
for i in bucket:
    if len(i)==0:
        bucket.remove(i)
print(bucket)
print(bucket[len(bucket)-k])


#k th largest number with duplicates
arr = [4,2,1,4,5,6,6,7,8,8,7,9,8,9]
k = 3
b = [0 for i in range(max(arr)+1)]
print(b)
for i in arr:
    b[i]+=1
print(b)
for i in range(len(b)-1,-1,-1):
    if b[i] != 0:
        k = k - b[i]
    if k <= 0:
        print(i)
        break

#kth highest largest freequency
arr = [0,2,2,2,3,3,4,4,4]
freq = {}

for i in arr:
    if i in freq:
        freq[i]+=1
    else:
        freq[i] = 1
print(freq)
m = 0
for i in freq:
    if freq[i]>m:
        m = freq[i]
        res = i
for i in freq:
    if freq[i]==m:
        print(i)
#print(res)


arr = [4,2,1,4,5,6,6,7,8,8,7,9,8,9]
freq = {}
k=3
for i in arr:
    if i in freq:
        freq[i]+=1
    else:
        freq[i] = 1
print(freq)
m = max(freq.values())
b = [0 for i in range(m+1)]
for i in freq:
    b[freq[i]] = i
print(b[-k])

#more's otique algorithm
ip = [2,1,1,2,3,1,1]
freq = {}
m = len(ip)//2
for i in ip:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
    if freq[i]>m:
        print(i)
print(freq)

   
ip = [2,2,2,2,3,1,1]
c=0
curr = 0
for i in range(len(ip)//2):
    if ip[i] == ip[i+1]:
        c+=1
        curr = ip[i]
    else:
        c-=1
        curr = ip[i]
    if c == 0:
        curr=ip[i]
print(curr)


#linear search
arr = [2,4,3,1,4,2,3,4,5]
k = 4
for i in range(len(arr)-1,-1,-1):
    if arr[i]==k:
        print(i)
        break
    
else:
    print("-1")



#binary search 
arr=[2,3,5,6,7,7,8,9,10,10,10,13,15]
k =7
l,r=0,len(arr)-1

while l<=r:
    m=(l+r)/2
    if arr[m]==k:
        print("found")
        break
    if k<arr[m]:
        r = m-1
    else:
        l=m+1


#binary search finding highest found occurance index
arr=[2,3,5,6,7,7,8,9,10,10,10,13,15]
k =7
l,r=0,len(arr)-1
re = -1
while l<=r:
    m=(l+r)//2
    if arr[m] == k:
        re = m
        l = m+1
    if k<arr[m]:
        r = m-1
    else:
        l=m+1    
    
print(re)    



#if element is found return the index of element if not return the element index where thenele should be
#it is sorted array
arr = [2,4,8,10,13,15]
k = 11
l,r=0,len(arr)-1
re = 0
while l<=r:
    m=(l+r)//2
    if arr[m] == k:
        re == 1
        print(m)
        break
    if k<arr[m]:
        r = m-1
    else:
        l=m+1    
    
if re == 0:
    print(m)

'''

#binary search 
arr=[2,3,5,6,7,7,8,9,10,10,10,13,15]
k =7
l,r=0,len(arr)-1

while l<=r:
    m=(l+r)//2
    if arr[m]==k:
        print("found")
        break
    elif k<arr[m]:
        r = m-1
    else:
        l=m+1







    
    

    
















