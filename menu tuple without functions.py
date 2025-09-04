x=()
y=()
n=int(input("enter number of elements:"))
print("enter elements:")
for i in range(n):
    x=int(input())
    y=y+(x,)
print(y)
print("1.maximum")
print("2.minimum")
print("3.average")
print("4.sort-ascending")
print("5.sort-descending")
choice=int(input("enter your coice:"))
if choice==1:
    print("maximum element:",max(y))
elif choice==2:
    print("minimum element:",min(y))
elif choice==3:
    print("average:",sum(y)/n)
elif choce==4:
    print("sort ascending:",sorted(y))
elif choice==5:
    print("sort descending:",sorted(y.reverse==true))
else:
    print("your choice is invalid.")
