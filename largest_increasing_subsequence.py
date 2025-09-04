arr = [1,2,3,4,5]
def longest(arr):
    n = len(arr)
    count = 1
    maxx = 1
    for i in range(0,n-1):
        if arr[i]+1 == arr[i+1]:
            count += 1
        else:
            maxx = max(maxx,count)
            count = 1
    maxx = max(maxx,count)
    return maxx
print(longest(arr))

'''
n = len(arr)
count = 1
maxx= 1
for i in range(0,n-1):
    if arr[i]+1 == arr[i+1] :
        count+=1
    else:
        maxx=max(maxx,count)
        count = 1
print(maxx)
'''

'''
#using listt
count = 1
listt = []
for i in range(0,n-1):
    if arr[i+1] - arr[i] == 1:
        count+=1
    else:
        if count > 1:
            listt.append(count)
            count = 1
print(max(listt))'''
