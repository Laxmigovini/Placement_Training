n=int(input("enter n value:"))
t=n
k=0
s=0
while(t!=0):
    t=t/10
    k=k+1
t=n
while(t!=0):
    r=t%10
    p=1
    j=1
    while(j<=k):
        p=p*r
        j=j+1
        s=s+p
        t=t/10
        if(s==n):
            print("it is amstrong number" %n)
        else:
            print("it is not amstrong number" %n)
