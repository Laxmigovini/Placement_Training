a = [1, 2, 3, 4, 5, 6]
n = 4
l = 0
r = len(a) - 1
while l <= r:
    m = (l+r)//2
    if a[m] == n:
        print(m)
        break
    elif a[m] < n:
        l = m+1
    else:
        r = m-1
        