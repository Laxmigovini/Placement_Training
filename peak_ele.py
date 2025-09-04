a = [1,2,3,4,5,6,7]
l = 0
r = len(a) -1
while l < r:
    m = (l+r)//2
    if a[m]<a[m+1]:
        l = m + 1
    else:
        r = m
print(a[l])