a = [2,4,3,1,4,2,3,4,5]
x = 4
for i in range(len(a)-1,-1,-1):
    if a[i] == x:
        print(i)
        break

