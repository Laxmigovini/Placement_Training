def div(a,b):
    d=a/b
    print("the division is:",d)
def mult(a,b):
    m=a*b
    print("the multiplication is:",m)
def add(a,b):
    c=a+b
    print("the addition is:",c)
def sub(a,b):
    s=a-b
    print("the subtraction is:",s)
import calc
m=int(input("enter m value:"))
n=int(input("enter n value:"))
calc.add(m,n)
calc.mult(m,n)
calc.add(m,n)
calc.sub(m,n)
