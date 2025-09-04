class rectangle: 
    def __init__(self,a,b): 
        self.height=a 
        self.width=b 
    def display(self): 
        print("Rectangle height =",self.height) 
        print("Rectangle width =",self.width) 
        ar=self.height*self.width 
        print("Area of rectangle is =:",ar) 
h=int(input("Enter h value")) 
w=int(input("Enter w value")) 
rect=rectangle(h,w) 
rect.display() 
print("") 
print("Changing the class variables values from outside the class:") 
print("") 
he=int(input("Enter h value")) 
wi=int(input("Enter w value")) 
rect.height=he 
rect.width=wi 
rect.display() 
#Using Private (Encapsulation) 
#Private 
class encap: 
    __a=10 #private Variable 
def __display(self): #private method
 print("Welcome to SRU")
 print(self.__a)
 obj = encap()
 obj.__display()
 
