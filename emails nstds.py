n=int(input("Enter number of email ids="))
l=[]
for i in range(n):
    l.append(input("Enter email ids="))
print(l)
a=tuple(l)
print(a)
pos=[]
luser=[]
ldomain=[]
for i in range(n):
    pos.append(l[i].index("@"))
for i in range(n):
    luser.append(l[i][:pos[i]])
    ldomain.append(l[i][pos[i]:])
tuser=tuple(luser)
tdomain=tuple(ldomain)
print(tuser)
print(tdomain)
