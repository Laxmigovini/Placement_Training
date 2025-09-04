'''a=int(input("enter first number:"))
b=int(input("enter second number:"))
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b)
print(a//b)  

#2. RELATIONAL OPERATORS
a=10
b=20
print(a==b)
print(a!=b)
print(a<b)
print(a>b)
print(a<=b)
print(a>=b)   


#3. LOGICAL OPERATORS
a=10
b=20
print(a<b and a==b)
print(a!=b or a<=b)
print(not(a>=b))


print(10>5  and 20>10  and 1>2)
print(10>5 or 20<10)
print(not(55==55))



a=True
b=False
c=True
print(a<b or b <c)
print(a<b and b<c)
print(not(a<b or b<c))



#BITWISE
a=10
b=20
print(a&b)
print(a|b)
print(a^b)
print(a>>b)
print(a<<b)
print(~b)
print(~a)
print(4<<1)
print(4<<2)
print(4<<3)
print(4>>1)
print(4>>2)
print(4>>3)


print(~10)

a=int(input("enter the age of person:"))
if(a<=12):
    print("child")
elif(a>12 and a<=19):
    print("teenager")
elif(a>19 and a<=59):
    print("adult")
else:
    print(senior)

a=int(input("enter a number:"))
if(a%2==0):
    print("it is divisible by 2")
elif(a%3==0):
    print("it is divisible by 3")
else:
    print("it is not divisible by 2 and 3")

char =input().lower()
if char in 'aeiou':
    print("vowel")
elif char.isalpha():
    print("consonant")
else:
    print("not a letter")

a=int(input("enter the marks of a stud:"))
if(a>=90):
    print("A")
elif(a<90 and a>=80):
    print("B")
elif(a<80 and a>=70):
    print("C")
elif(a<70 and a>=60):
    print("D")
else:
    print("Fail")


a=int(input("enter a num:"))
if(a%2==0):
    print("even")
else:
    print("odd")


day=int(input("enter the number:"))
if day == 1:
    print("monday")
elif day ==2:
    print("tuesday")
elif day == 3:
    print("wednesday")
elif day == 4 :
    print("Thursday")
elif day ==5 :
    print("Friday")
elif day ==6 :
    print("Saturday")
else:
    print("sunday")

a= int(input("enter a number:"))
if(a%5==0 and a%7==0):
    print("number is divisible by both 5 and 7")
elif(a%5==0):
    print("divisible by 5")
elif(a%7==0):
    print("divisible by 7")
else:
    print("not divisible by any number")'''
































