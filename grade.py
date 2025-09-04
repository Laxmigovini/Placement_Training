sub1=int(input("enter sub1 marks:"))
sub2=int(input("enter sub2 marks:"))
sub3=int(input("enter sub3 marks:"))
sub4=int(input("enter sub4 marks:"))
total=sub1+sub2+sub3+sub4
avg=total/4
if(avg>=80):
    print("Agrade!")
elif(avg>=60 and avg<80):
    print("B grade!")
elif(avg>=40 and avg<60):
    print("C grade!")
else:
    print("FAIL")
