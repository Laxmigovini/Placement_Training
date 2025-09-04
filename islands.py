mat = [[1,0,0,1,1],[1,0,0,0,1],[1,0,0,0,0],[1,0,0,0,0],[1,0,0,0,1]]
def island(mat,i,j,n):
    if i < 0 or j < 0 or i == n or j == n or mat[i][j] == 0 or mat[i][j] == 2:
        return 0
    if mat[i][j] == 1:
        mat[i][j] = 2
        island(mat,i-1,j,n)
        island(mat,i+1,j,n)
        island(mat,i,j-1,n)
        island(mat,i,j+1,n)
c = 0
for i in range(5):
    for j in range(5):
        if mat[i][j] == 1:
            island(mat,i,j,5)
            c+=1
print(c)
