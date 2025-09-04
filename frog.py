a = [(2,1),(4,1),(5,2),(3,5)]
def frog(a,i=0,j=0,n=5):
    if i == n or j == n or (i,j) in a:
        return 0
    if i == n-1 and j == n - 1:
        return 1
    return frog(a,i+1,j,n)+frog(a,i,j+1,n)
print(frog(a,1,2))
