'''
ip = "abcdecfbgce"
maxi = 0
l,r = 0,0
freq = {}

for r in range(len(ip)):
    if ip[r] not in freq:
        freq[ip[r]]=r
        maxi = max(maxi,r-l+1)
    elif freq[ip[r]]>=l and ip[r] in freq:
        l = freq[ip[r]]+1
        freq[ip[r]]=r
        
print(freq)
print(maxi)

#longest substring without repeating characters and m,n should contain in it
ip = "abcdecfbgce"
m = 'a'
n = 'b'
maxi = 0
l,r = 0,0
freq = {}
for r in range(len(ip)):
    if ip[r] not in freq:
        freq[ip[r]] = r   
    else:
        if freq[ip[r]]>=l :
            l = freq[ip[r]]+1
        freq[ip[r]] = r
        
    if m in freq and n in freq and freq[m]>=l and freq[n]>=l:
        maxi = max(maxi,r-l+1)
            
            
print(maxi)


#in the deck of cards find the maxi sum when cards removed from front and last
ip = [4,3,2,5,6,1,12,3]
k = 3
maxi = 0

for i in range(k+1):
    if i == k:
        total = sum(ip[:i])
    else:
        front=ip[:i]              
        back=ip[-(k-i):]        
        total=sum(front)+sum(back)
    
    maxi=max(maxi,total)
        
print(maxi)

ip = [4,3,2,5,6,1,12,3]

n = len(ip)

k = 3
sl = 0
for i in range(k):
     sl = sl+ip[i]
print(sl)
sr = 0
m = sl
for i in range(k-1,-1,-1):
    sl = sl-ip[i]
    sr = sr +ip[n-1]
    m = max(m,sl+sr)
    n-=1
print(sr)
print(m)




ip = [1,1,1,0,0,0,1,1,1,1,0]
l = 0
z = 0
k = 2
m = 0
for r in range(len(ip)):
     if ip[r] == 0:
          z = z+1
     if z>k:
          if ip[l] == 0:
               z = z-1
          l = l+1
     if z<=k:
          m = max(m,r-l+1)
print(m)
 '''

ip1 = [900,945,1110,1230,1235,1245,1340,1700]
ip2 = [930,1130,1120,1250,1250,1415,1400,1730]
ip1.sort()
ip2.sort()
print(ip1)
print(ip2)
#[900, 945, 1110, 1230, 1235, 1245, 1340, 1700]
#[930, 1120, 1130, 1250, 1250, 1400, 1415, 1730]

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
#[900, 930, 945, 1110, 1120, 1130, 1230, 1235, 1245, 1250, 1250, 1340, 1400, 1415, 1700, 1730]
l= 0
c = 0
for r in range(ip):
     if ip[r] 






































     




















