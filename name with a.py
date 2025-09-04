n = int(input("Enter number of elements:"))
a = []
print("Enter the names:")
for i in range(n):
    a.append(input("Enter a name:"))
print(a)
print("The names which are starts with a is:")
for j in a:
    if j[0] == 'a':
       print(j)

