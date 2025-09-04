a=[9,9,8,7,6,5,4,3,2,1]
def mergesort(a):
    if len(a) <= 1:
        return a
    mid = len(a) // 2
    l = mergesort(a[:mid])
    r = mergesort(a[mid:])
    return merge(l,r)
def merge(left,right):
    i=0
    j=0
    res = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i+=1
        else:
            res.append(right[j])
            j+=1
    res.extend(left[i:])
    res.extend(right[j:])
    return res
print(mergesort(a))