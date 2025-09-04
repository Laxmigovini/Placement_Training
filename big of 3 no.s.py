x=float(input("enter first number:"))
y=float(input("enter secnd number:"))
z=float(input("enter third number:"))
if(x>-y)and(x>=z):
    big_value=x
elif(y>=x)and(y>=z):
    big_value=y
else:
    big_value=z
    print("the big_value number is",big_value)
