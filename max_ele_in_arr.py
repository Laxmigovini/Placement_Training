arr = [2, 7, 1, 9, 5]
maxi = 0
for i in range(len(arr)-1):
    if arr[i] > maxi:
        maxi = arr[i]
print(maxi)