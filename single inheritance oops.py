#parent class 
class student: 
    def calculate(self,a,b,c): 
        self.a=a 
        self.b=b 
        self.c=c 
        self.s=a+b+c 
        print("Sum of three numbers is= ",self.s)         
#child class 
class student_child(student): 
     def show(self): 
         print("I am show method of child class") 
#creating the instance of the child/derived class 
x=int(input("Enter first number: ")) 
y=int(input("Enter second number: ")) 
z=int(input("Enter third number: ")) 
c1=student_child() 
c1.calculate(x,y,z) 
c1.show() 
