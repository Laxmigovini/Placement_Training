'''arr = [1,1,2,3,3,4,4,5,5,8,8]
n = len(arr)
for i in range(0,n-1,2):
    if arr[i] != arr[i+1]:
        print(arr[i])
        break
else:
    print(arr[-1])
    '''
arr = [1,2,3,2,1,3,4,5,6,6,5,6,7,7]
freq={}
for i in arr:
    if i in freq:
        freq[i]+=1
    else:
        freq[i] = 1
for key,value in freq.items():
    if value == 1:
        print(key)