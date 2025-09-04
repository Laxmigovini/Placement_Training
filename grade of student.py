name=input("enter your name:")
htno=input("enter your hallticket number")
course=input("enter your course")
print("name:",name)
print("htno:",htno)
print("course:",course)
sub1=int(input("enter sub1 marks:"))
sub2=int(input("enter sub2 marks:"))
sub3=int(input("enter sub3 marks:"))
sub4=int(input("enter sub4 marks:"))
sub5=int(input("enter sub5 marks:"))
total=sub1+sub2+sub3+sub4+sub5
print("sum of 5 subjects:",total)
avg=total/5
print("avg of 5 subjects:",avg)
if(avg>=80):
    print("A GRADE!")
elif(avg>=60 and avg<40):
    print("Bgrade")
elif(avg>=40 and avg<20):
    print("Cgrade")

else:
    print("FAIL")    
if(sub1<40):
    print("fail")
elif(sub2<40):
    print("fail")
elif(sub3<40):
    print("fail")
elif(sub4<40):
    print("fail")
else:
    print("fail")
