import math
piles = [30,11,23,4,20]
h = 5
l = 1
r = max(piles)
while l < r:
    m = (l+r) // 2
    s=0
    for i in piles:
        s += math.ceil(i/m)
    if s > h:
        l = m + 1
    if s <= h:
        r = m
print(l)





'''k = 1
while 1:
    s=0
    for i in piles:
        s+=math.ceil(i/k)
        if s > h:
            k+=1
            break
    else:
        print(k)
        break'''
'''while l < r:
    s = 0
    for i in piles:
        m = (l+r)//2
        s += math.ceil(i/m)
    if s <= h:
        r = m
    if s > h:
        l = m + 1
print(l)'''