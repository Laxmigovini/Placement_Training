n=int(input("enter n value"))
t=n
s=0
while(t!=0):
    r=t%10
    s=s*10+r
    t=t/10
    print("reverse of a number:",s)
