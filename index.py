numb=tuple()
n=int(input("enter no.of elements:"))
for i in range(0,n):
    num=int(input("enter elements:"))
    numb=numb+(n,)
print(numb)
i=int(input("enter a number:"))
print(i in numb)
for num in numb:
    num.index(i)
print()
