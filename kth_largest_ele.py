a = [2,5,8,6,3,1,9,4,7]
'''def kth_largest_ele(a,k):
    n = len(a)
    for i in range(n-1):
        for j in range(n-i-1):
            if a[j] > a[j+1]:
                a[j],a[j+1] =a[j+1],a[j]
        if i == k:
            return a[n-i]
print(kth_largest_ele(a,4))'''
def kthlargest(a,k):
    return sorted(a,reverse=True)[k-1]
print(kthlargest(a,4))

