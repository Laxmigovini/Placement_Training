
n = int(input("How many names you want to enter : "))
name = ()
for i in range(n):
    nm = input("Enter name : ")
    name = name + (nm,)
    nm = input("Enter name to search : ")
if nm in name:
    print("name is present in tuple",nm)
else:
    print("name is not found in tuple",nm)
