n = int(input())
i = 0
while n:
    if 2**i == n:
        print("yes")
        break
    i+=1
    if 2**i > n:
        print("no")
        break
    