a=0
b=1
c=0
print("enter the value of n:",end="")
n=int(input())
a=int(input())
b=int(input())
c=int(input())
print("\n fibonacci series:",a,b,end="")
c=a+b
n=n-2
while(n>0):
    print(c,end="")
    a=b
    b=c
    c=a+b
    n=n-1
