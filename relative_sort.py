a1 = [2,3,1,3,2,4,6,7,9,2,19]
a2 = [2,1,4,3,9,6]
res = []
for i in a2:
    count = a1.count(i)
    res += [i] * count
    for _ in range(count):
        a1.remove(i)
a1.sort()
res += a1
print(res)
