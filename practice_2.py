'''start = [0,3,8,1,5,7,9]
end = [5,6,10,2,6,9,11]
def fun(x):
    return x[1]
lis = []
for i,j in zip(start,end):
    lis.append((i,j))
print(lis)
lis.sort(key = fun)
print(lis)
c= 0
st = 0
for i in lis:
    if i[0] >= st:
        c += 1
        st = i[1]+1
print(c)
'''
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
    
