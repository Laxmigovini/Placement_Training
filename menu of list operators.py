#Menu driven program to do various list operations
'''1. Maximum
2. Minimum
3. sum
4. average
5. sort - Ascending
6. sort - Descending
7. Exit'''
n = int(input("Enter number of elements:"))
a = []
for i in range(n):
    a.append(int(input("Enter Element:")))
print(a)
print("1. Maximum")
print("2. Minimum")
print("3. sum")
print("4. average")
print("5. sort - Ascending")
print("6. sort - Descending")
print("7. Exit")
while(input("Do You want to continue [y/n]:") == 'y'):
     choice = -1
     choice = int(input("Enter Your Choice:"))
if choice == 1:
   print("Maximum Element is:",max(a))
elif choice == 2:
   print("Minimum Element is:",min(a))
elif choice == 3:
    print("Sum of Element is:",sum(a))
elif choice == 4:
    print("Average is:",sum(a)/len(a))
elif choice == 5:
   a.sort()
   print("Ascending order Sorting is:",a)
elif choice == 6:
     a.sort(reverse=True)
     print("Descending order Sorting is:",a)
elif choice == 7:
     quit()
else:
    exit()

