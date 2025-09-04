a1=[2,4,5,8,9]
a2=[3,5,6,9,11,12,13]
i=0
j=0
res = []
while i < len(a1) and j < len(a2):
    if a1[i] < a2[j]:
        res.append(a1[i])
        i+=1
    else:
        res.append(a2[j])
        j+=1
res.extend(a1[i:])
res.extend(a2[j:])
print(res)