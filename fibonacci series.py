n=int(input("enter number of terms in fibonacci series:"))
t1=0
t2=1
t=t1+t2
i=3
print("fibonacci series of %d terms :\n%d\n%d"%(n,t1,t2))
while(i<=n):
    print(" ",t)
    t1=t2
    t2=t
    t=t1+t2
    i=i+1
