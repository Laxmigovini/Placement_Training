#Write a python program to demonstrate Multiple Inheritance 
#Creating the Base classes 
class operation1: 
   def sum(self,a,b): 
       return a+b 
class operation2: 
   def sub(self,a,b): 
       return a-b 
class operation3: 
   def div(self,a,b): 
       return a/b 
class operation4: 
   def mult(self,a,b): 
       return a*b     
#creating derived or child class  
class calculate(operation1,operation2,operation3,operation4): 
    def mod(self,a,b): 
        return a%b 
#creating the object of child class 
c=calculate() 
a=int(input("Enter the first number: ")) 
b=int(input("Enter the second number: ")) 
print("The Sum of two number(a+b)= ",c.sum(a,b)) 
print("The Subtraction of two number(a-b)= ",c.sub(a,b)) 
print("The Division of two number(a/b)= ",c.div(a,b)) 
print("The Multiplication of two number(a*b)= ",c.mult(a,b)) 
print("The Modulous of two number(a%b)= ",c.mod(a,b)) 
