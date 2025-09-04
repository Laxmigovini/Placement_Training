n=int(input("enter n value:"))
t=n
s=0
while(t!=0):
    r=t%10
    s=s*10+r
    t=t/10
    if(s==n):
        print("%d is a palindrome"%n)
    else:
      print("%d is not a palindrome"%n)
