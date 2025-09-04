a = [9,8,7,6,5,4,3,2,1]
n = len(a)
for i in range(n):
    minidx = i
    for j in range(i+1,n):
        if a[j] < a[minidx]:
            minidx = j
    a[i],a[minidx] = a[minidx],a[i]
print(a)