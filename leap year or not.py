y=int(input("enter the y:"))
if(y%4==0)and(y%100==0):
    print("{0} is a leap y".format(y))
else:
    print("{0} is not a leap year".format(y))
