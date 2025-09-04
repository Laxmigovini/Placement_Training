'''for i in range(1,11):
    print(i)
for i in range(1,21):
    if (i%2==0):
        print(i)
sum=0
for i in range(1,101):
    sum+=i
print(sum)
str=input()
str2=str[::-1]
print(str2)
a=int(input())
if(a<0):
    print("doesnot exist")
elif(a==0):
    print("0")
else:
    fact=1
    for i in range(1,a+1):
        fact*=i
    print(fact)
a=int(input("enter number:"))
for i in range(1,11):
    print(f"{a}*{i}={a*i}")

string=input()
count=0
str2="aeiou"
for i in string:
    if i in str2:
        count+=1
print(count)

a= int(input("enter a number:"))
prime=True
for i in range(2,a):
    if a%i==0:
        prime=False
    break
if (prime):
    print("it is a prime number")

a=0
b=1
n=int(input("enter the range"))
for i in range(n):
    print(a)
    a,b  = b , a + b

a=int(input("enter the no. of rows:"))
for i in range(a):
    for j in range(a-i-1):
        print(" ",end="")
    for j in range(2*i+1):
        print("*",end="")
    print()

for i in range(10,0,-1):
    print(i)

a=int(input("enter a number:"))
sum=0
for i in str(a):
    sum+=int(i)
print(sum)

a=int(input("enter a number:"))
length=len(str(a))
result=0
for i in str(a):
    result+=int(i)**length
if result==a:
    print("armstrong number",result)
else:
    print("not an armstrong number")

a=int(input("enter a number:"))
prime=True
for i in range(2,50):
    for i in range(2,a):
        if(a%2==0):
            prime=False
        break
if(prime):
    print("prime number")
else:
    print("Not a prime number")'''
        








    
    






    
