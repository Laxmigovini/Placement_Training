'''a = [9,8,5,6,4,8]
n = len(a)
for i in range(n):
    flag = 0
    for j in range(i+1,n):
        if a[i] > a[j]:
            a[i],a[j] = a[j],a[i]
            flag = 1
    if flag == 0:
        break
print("sorted_array:",a)'''


a = ['d', 'b', 'a', 'c', 'e']
n = len(a)
for i in range(n):
    flag = 0
    for j in range(0,n-i-1):
        if a[j] > a[j+1]:
            a[j],a[j+1] = a[j+1],a[j]
            flag = 1
    if flag == 0:
        break
print(a)