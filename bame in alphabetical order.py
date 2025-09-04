n=int(input("enter number of names:"))
name=[]
for i in range(n):
    name.append(str(input("enter name:")))
print("names:")
for i in range(n):
    print(name[i])
    print()
name.sort()
print("names with alphabetical ordera:")
for i in range(n):
    print(name[i])
    print()
name=tuple()
print(name)
