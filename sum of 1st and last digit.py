print("enter a number:")
num=int(input())
count=0
while(num!=0):
    if(count==0):
        last=num%10
        count=count+1
        rem=num%10
        num=int(num/10)
        sum=rem+last
    print("\nsum of first and last digit=",sum)
