a = [1,2,3,4,5,6,7,8]
maxx = float('-inf')
maxx1 = float('-inf')
for i in range(len(a)):
    if a[i] > maxx:
        maxx1=maxx
        maxx = a[i]
    elif a[i] > maxx1 and a[i] != maxx:
        maxx1 = a[i]
print(maxx)
print(maxx1)
