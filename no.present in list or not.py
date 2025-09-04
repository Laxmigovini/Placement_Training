n= int(input("Enter number of elements:"))
a = []
print("Enter Elements:")
for i in range(n):
    a.append(int(input()))
print(a)
position = -1
search = int(input("Enter a element to be search:"))
for i in range(n):
    if a[i] == search:
        position = i+1
if position == -1:
    print("Element is not found")
else:
    print("Element",search,"found at position",position)

