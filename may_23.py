'''
#find the maximum number of meetings occured.(using greedy)
def fun(x):
    return x[1]
start = [0,3,8,1,5,7,9]
end = [5,6,10,2,6,9,11]
b =[]
for i,j in zip(start,end):
    b.append((i,j))
print(b)
b.sort(key = fun)
print(b)
st = 0
c=0
for i in b:
    if i[0]>=st:
        c+=1
        st=i[1]+1
print(c)


ip= "hippoPotamus"
ip1 = list(ip)
i,j = 0,len(ip1)-1
vowels = "AEIOUaeiou"
while i<j:
    if ip1[i] not in vowels and ip1[j] not in vowels:
        ip1[i],ip1[j] = ip1[j],ip1[i]
        i+=1
        j-=1
    elif ip1[i] not in vowels:
        j-=1
    elif ip1[j] not in vowels:
        i+=1
    else:
        i+=1
        j-=1
print("".join(ip1))
        



ip = [2,1,6,4,2,3,1,1,4,2,6,7,3]
k = 5
maxi = 0
for i in range(len(ip)-k+1):
    summ = sum(ip[i:i+k])
    maxi = max(maxi,summ)
print(maxi)
  
ip = [2,1,6,4,2,3,1,1,4,2,6,7,3]
k = 5
maxi = -1234
for i in range(len(ip)-1):
    s = 0
    for j in range(i,len(ip)):
        s = s+ip[j]
        if s <= k:
            maxi = max(maxi,j-i+1)
        else:
            break
print(maxi)

ip = [2,1,6,4,2,3,1,1,4,2,6,7,3]
k = 5
maxx = 0
s =0
i,j = 0,0
while j <= len(ip)-1:
    s = s + ip[j]
    if s <=k:
        maxx = max(maxx,j-i+1)
        j+=1
    else:
        s-=ip[i] #here we are moving i so we have to subtract.
        i+=1
        j+=1
print(maxx)
        

#length of longest palindrome substring
ip = "ababba"
n = len(ip)
maxi = 0
for i in range(n):
    l = i
    r = i
    while l>=0 and r <len(ip) and ip[l]== ip[r]:
        maxi = max(maxi,r-l+1)
        l = l-1
        r = r+1
    l,r = i,i+1
    while l>=0 and r <len(ip) and ip[l]== ip[r]:
        
        maxi = max(maxi,r-l+1)
        l = l-1
        r = r+1
print(maxi)
 
#print the longest substring
ip = "ababba"
n = len(ip)
m = 0
st = 0
for i in range(n):
    l = i
    r = i
    while l>=0 and r <len(ip) and ip[l]== ip[r]:
        if r-l+1 > m:
            m = r-l+1
            st = l 
        l = l-1
        r = r+1
    l,r = i,i+1
    while l>=0 and r <len(ip) and ip[l]== ip[r]:
        
        if r-l+1 > m:
            m = r-l+1
            st = l
        l = l-1
        r = r+1
print(ip[st:st+m])     
   
    
ip = "ababba"
n = len(ip)
m = 0
st = 0
count = 0
for i in range(n):
    l = i
    r = i
    while l>=0 and r <len(ip) and ip[l]== ip[r]:
        if r-l+1 > m:
            m = r-l+1
            st = l
        count = count+1
            
        l = l-1
        r = r+1
    l,r = i,i+1
    while l>=0 and r <len(ip) and ip[l]== ip[r]:
        
        if r-l+1 > m:
            m = r-l+1
            st = l
        count = count+1
        l = l-1
        r = r+1
print(count)    
 


ip = "abcdaecdb"
m = 0
n = len(ip)
l,r = 0,0

while l>=0 and r <len(ip):
    if ip[r] not in ip[l:r]:
        m = max(m,r-l+1)
        r+=1
    else:
        l = l+1
print(m)



ip = "abcdecfbgce"
maxi = 0
l,r = 0,0
freq = {}
lis = 0
for r in range(len(ip)):
    if ip[r] not in freq:
        freq[ip[r]]=r
        maxi = max(maxi,r-l+1)
    elif freq[ip[r]]>=l and ip[r] in freq:
        l = freq[ip[r]]+1
        freq[ip[r]]=r
        
print(freq)
print(maxi)

'''


















        










    
            
            

        
