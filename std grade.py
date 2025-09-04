name=input("enter name of student")
htno=input("enter hallticket number of the student")
cr=input("enter the course")
print("enter marks obtained in 5 subjects:")
m1=int(input())
m2=int(input())
m3=int(input())
m4=int(input())
m5=int(input())
print("name of the student is=",name)
print("hallticket number is",htno)
print("course is=",cr)
tot=m1+m2+m3+m4+m5
print("total marks are",tot)
avg=tot/5
print("average is",avg)
if(avg>=91)and (avg<=100):
    print("your grade is A1")
elif(avg>=81)and(avg<91):
    print("your grade is A2")
elif(avg>=71)and(avg<81):
    print("your grade is B1")
elif(avg>=61)and(avg<71):
    print("your grade is B2")
elif(avg>=51)and(avg<61):
    print("your grade is C1")
elif(avg>=41)and(avg<51):
    print("your grade is C2")
elif(avg>=33)and (avg<41):
    print("your grade is D")
elif(avg>=21)and(avg<33):
    print("your grade is E1")
elif(avg>=0)and(avg<21):
    print("your grade is E2")
else:
    print("invalid input!")
 
