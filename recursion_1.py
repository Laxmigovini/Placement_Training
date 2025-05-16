arr = [2,4,6,3,3,2,6,1,2,3,6,6,5]
'''
def count(arr,k,i=0,c=0):
    if i == len(arr):
        return c
    if arr[i] == k:
        c += 1
    return count(arr,k,i+1,c)
#k = int(input())        
#print(count(arr,k))

arr = [2,4,6,3,3,2,6,1,2,3,6,6,5]
def count(arr,k,i=0):
    if i == len(arr):
        return 0
    if arr[i] == k:
        return 1+ count(arr,k,i+1)
    return count(arr,k,i+1)
#k = int(input())        
#print(count(arr,k))


def freequency(arr,f,i=0):
    if i == len(arr):
        return 0
    if (count(arr,arr[i]) == f):
        return arr[i]
    return freequency(arr,f,i+1)

f = int(input())
print(freequency(arr,f))

def value(a,f,d,i=0):
    if(i==len(a)):
        return "not found"
    if d[a[i]] == f:
        return a[i]
    return value(a,f,d,i+1)
def freq_d(a,f,d={},i=0):
    if (i == a[i]):
        return value(list(d.keys()),f,d)
    if a[i] not in d:
        d[a[i]] = 1
    else:
        d[a[i]]+=1
    return freq_d(a,f,d,i+1)
a = [2,4,6,3,3,2,6,1,2,3,6,6,5]
f = int(input())
print(freq_d(a,f))


def subset(arr,listt=[],i = 0):
    if i == len(arr):
        print(listt)
        return 
    subset(arr,listt+[arr[i]],i+1)
    subset(arr,listt,i+1)
arr = [2,3,4]
print(subset(arr))

def subset_sum(arr,k,i=0):
    if k == 0:
        return True
    if i == len(arr):
        return False
    if arr[i]>k:
        return subset_sum(arr,k,i+1)
    return subset_sum(arr,k,i+1) or subset_sum(arr,k-arr[i],i+1)
arr = [2,3,4]
k = 6
print(subset_sum(arr,k))
    
        
def subset_sum(arr,k,i=0):
    if i == len(arr):
        return k == 0
    return subset_sum(arr,k,i+1) or subset_sum(arr,k-arr[i],i+1)
arr = [2,3,4]
k = 6
print(subset_sum(arr,k))
           
def subset(arr,k,listt=[],i = 0):
    if i == len(arr):
        if k == 0:
            print(listt)
        return
    if arr[i]<=k:
        subset(arr,k-arr[i],listt+[arr[i]],i+1)
    subset(arr,k,listt,i+1)
        
arr = [1,2,3,5]
k = 7
subset(arr,k)


def subset_len(arr,k,listt = 0,i = 0,minn=9999999):
    
    if i == len(arr):
        if k == 0:
            if (minn > listt):
                minn = listt
        
        return minn
    if arr[i]<=k:
        minn = subset_len(arr,k-arr[i],listt+1,i+1,minn)
    minn = subset_len(arr,k,listt,i+1,minn)
    return minn

arr = [1,2,3,5]
k = 7
print(subset_len(arr,k))

#we should not use recursion for coins - use tabulation that is dynamic programming.


listt = list(map(int,input().split()))
maxx = 0
minn = 9999999
for i in range(len(listt)):
    if listt[i] % 2 == 0:
        if maxx < listt[i]:
            maxx = listt[i]
    if listt[i] % 2 !=0:
        if minn > listt[i]:
            minn = listt[i]
    
print(maxx)
print(minn)

def recursion(listt,maxx = 0,minn = 999999,i=0):
    if i == len(listt):
        return maxx,minn
    
    if listt[i] % 2 == 0:
        if maxx < listt[i]:
            maxx = listt[i]
    if listt[i] % 2 !=0:
        if minn > listt[i]:
            minn = listt[i]
    return recursion(listt,maxx,minn,i+1)

listt = list(map(int,input().split()))
print(recursion(listt))

'''

listt = list(map(int,input().split()))
maxx = -1234
maxx1 = -1234

for i in range(len(listt)):
    if maxx < listt[i]:
        maxx1 = maxx
        maxx = listt[i]
    elif listt[i]!=maxx and listt[i]>maxx1:
        maxx1 = listt[i]
    
print(maxx1)

        
    

        
            





        













































    
    
    


