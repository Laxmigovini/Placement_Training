def searchname(t1,nm):
    for a in t1:
        if a == nm:
           print(nm , " Name is present in Tuple")
        return
print("Name not found")
n = int(input("How many names you want to enter : "))
name = ()
for i in range(n):
    nm = input("Enter name : ")
    name = name + (nm,)
    nm = input("Enter name to search : ")
    searchname(name, nm)

