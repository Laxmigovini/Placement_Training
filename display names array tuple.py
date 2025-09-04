name=input("Enter you name:")
l=len(name)
m=[]
for i in range(l):
    a=[]
    for j in range(l):
        a.append(name)
    m.append(a)
for i in range(l):
     for j in range(l):
         print(m[i][j],end=" ")
     print()
