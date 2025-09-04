a = [20,30,40,50,3,4,5,6,8]
l = 0
r = len(a)//2
while l<r:
    m = (l+r) // 2
    if a[m] > a[r]:
        l = m + 1
    else:
        r = m 
print(l)