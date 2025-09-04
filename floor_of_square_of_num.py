n = 110
for i in range(1,n//2):
    if i*i >= n:
        print(i-1)
        break
    if i*i > n:
        print(i-1)
        break
    