
#Menu driven program to do various list operations
'''1. Insert an Element
2. Insert an Element desired position
3. Update an Element
4. Delete an Element
5. Delete Element desired position
6. Display
7. Exit'''
n= int(input("Enter number of Elements you want:"))
a = []
for i in range(n):
    a.append(input("Enter Element:"))
print(a)
print("1. Insert an Element")
print("2. Insert an Element desired position")
print("3. Update an Element")
print("4. Delete an Element")
print("5. Delete Element desired position")
print("6. Display")
print("7. Exit")
choice = -1
while (input("do You want to continue [y/n]:") == "y"):
      choice = int(input("Enter Your choice:"))
if choice == 1:
    e = input("Enter element to be inserted:")
    a.append(e)
    print(a)
elif choice == 2:
         i = int(input("Enter the index position:"))
         e = input("Enter element to be inserted:")
         a.insert(i,e)
         print(a)
elif choice == 3:
          i = int(input("Enter the position:"))
          e = int(input("Enter element to be updated:"))
          a[i] = e
          print(a)
elif choice == 4:
     e= int(input("Enter element to be Deleted:"))
     a.remove(e)
     print(a)
elif choice == 5:
     i = int(input("Enter the index of element to be Deleted:"))
     a.pop(i)
     print(a)
elif choice == 6:
     print(a)
else:
  print("Enter the correct choice")




