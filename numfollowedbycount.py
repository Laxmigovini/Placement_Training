arr=[2,2,3,3,3,4,4,4,4,5,5,5,5,5,6,6,6,6,6,6]
n = len(arr)
listt = []
count = 1
for i in range(n-1):
    if arr[i] == arr[i+1]:
        count += 1
    else:
        listt.append(arr[i])
        listt.append(count)
        count = 1
listt.append(arr[i])
listt.append(count)
print(listt)

