n=int(input("enter number of names:"))
name=[]
x=list(n)
for i in range(n):
    name.append(str(input("enter name:")))
print("names:")
for i in range(n):
    print(name[i])
    print()
name.sort()
print("names with a:")
for i in range(n):
    print(name[i])
    print()
name=tuple()
print(name)
