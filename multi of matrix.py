r = int(input("Enter Number of rows:"))
c = int(input("Enter Number of colmns:"))
m1 = []
for i in range(r):
    a = []
    for j in range(c):
        a.append(int(input("Enter Elements:")))
    m1.append(a)
print("The Matrix M1 Is:")
for i in range(r):
    for j in range(c):
        print(m1[i][j],end=" ")
    print()
print("Enter Elements for Matrix M2:")
m2 = []
for i in range(r):
    b = []
    for j in range(c):
        b.append(int(input("Enter Elements:")))
    m2.append(b)
print("The Matrix M2 Is:")
for i in range(r):
    for j in range(c):
        print(m2[i][j],end=" ")
    print()
print("Multiplication of M3 = M1*M2 is:")
m3 = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(r):
    for j in range(c):
        for k in range(c):
            m3[i][j] = m3[i][j]+(m1[i][k]*m2[k][j])
for i in range(r):
    for j in range(c):
        print(m3[i][j],end=" ")
    print()
