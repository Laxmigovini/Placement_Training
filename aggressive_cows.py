a = [1,2,5,7,10,12]
mi = 0
l = 1
h = a[-1] - a[0]
while l <= h:
    k = 3
    c1 = a[0]
    cows = k-1
    for i in a[1:]:
        m = (l+h)//2
        if i - c1 >= m:
            c1 = i
            cows -= 1
    if cows <= 0:
        mi =m
        l = m +1
    else:
        h = m-1
print(mi)



'''mi = 5
while 1:
    cows = 3
    c1 = a[0]
    cows = cows - 1
    for i in a:
        if i - c1 >= mi:
            c1 = i
            cows = cows - 1
    if cows <= 0:
        mi += 1
        break
print(mi-1)'''
