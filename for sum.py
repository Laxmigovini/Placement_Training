print("enter the values:")
n=int(input())
m=int(input())
s=0
#for n in range(m):
 #   s=s+n
  #  print("sum is=",s)

for n in range(n,m):
    s=s+n
    if(s==3):
        break;
    print("sum is=",s)
 
else:
    print("end of program!")
