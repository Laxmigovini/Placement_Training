rows=int(input("input rows"))
columns=int(input("input columns"))
matrix=[[0]*columns for row in range(rows)]
print("input number of elements in a row:")
for row in range(rows):
    lines=list(map(int,input().split()))
    for column in range(columns):
        matrix [row][column]=lines[column]
sum=[0]*columns
print("sum of eac column:")
for column in range(columns):
    for row in range(rows):
        sum[column]+=matrix[row][column]
    print((sum[column]))
