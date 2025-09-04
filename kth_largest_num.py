a = [2,1,3,4,6,7,8,9]
def kth_largest_num(a,k):
    n = len(a)
    for i in range(n):
        for j in range(0,n-i-1):
            if a[j] > a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
        if i == k :
            return a[n-i]
print(kth_largest_num(a,4))