x=[[1,3],[4,5],[7,9]]
r=[[0,0,0],[0,0,0]]
for i in range(len(x)):
    for j in range(len(x[0])):
        r[j][i]=x[i][j]
for r in r:
    print(r)
