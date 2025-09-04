r=int(input())
c=int(input())
m1=[]
for i in range(r):
    a=[]
    for j in range(c):
        a.append(int(input("enter elements:")))
        m1.append(a)
print("matrix1 elements:")
for i in range(r):
    for j in range(c):
        print(m1[i][j],end="")
    print()
'''print("enter elements of matrix 2:")
m2=[]
for i in range(r):
    b=[]
    for j in range(c):
        b.append(int(input("enter elements:")))
        m1.append(b)
print("matrix2 elements:")
for i in range(r):
    for j in range(c):
        print(m1[i][j],end="")
    print()'''
for i in range(0,r):
    sumc=0
    for j in range(0,c):
        sumc=sumc+m1[i][j]
    print("sum of column elements:",sumc)
