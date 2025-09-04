age=int(input("enter your age:"))
if(age<18):
    print("you cannot apply for job!you are too young")
elif(age>=18 and age<=60):
    print("you can cast your job!")
else:
    print("you are too old! you canot apply for job")
