mat = [[1,0,0,0,0],[1,1,1,0,0],[1,0,1,0,0],[1,0,1,1,1],[1,1,1,1,1]]
def rats(mat,n,i=0,j=0):
    if i >=n or j >= n or mat[i][j] == 0:
        return 0
    if i == n -1 and j == n - 1 and mat[i][j] == 1:
        return 1
    return rats(mat,n,i+1,j) + rats(mat,n,i,j+1)
print(rats(mat,5))