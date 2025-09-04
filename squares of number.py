n=int(input("enter n value:"))
t=n
s=0
while(t!=0):
    r=t%10
    s+=(r*r)
    t=t/10
    print("sum of squares of a number\n%d=%d"%(n,s))
