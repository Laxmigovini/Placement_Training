#Base Class 
class Pet: 
    def __init__(self, pet_type, name, bdate): 
       self.pet_type = pet_type 
       self.name = name 
       self.bdate = bdate 
    def details(self): 
      print("I am pet") 
#Derived Class 1 
class Cat(Pet): 
    def __init__(self, pet_type, name, bdate): 
       self.name = "Grey " + name 
       self.pet_type = pet_type 
    def details(self): 
       print('I am cute pet', self.pet_type, 'people call me', self.name) 
#Derived Class 2 
class Dog(Pet): 
   def __init__(self, pet_type, name, bdate, breed): 
       super().__init__(pet_type, name, bdate) 
       self.breed = breed 
   def sounds(self, sound): 
       return sound 
  
   def details(self): 
       print('I am', self.name,',a', self.breed) 
pet1 = Pet('cat', 'Tiffiny', '2019-07-08') 
pet2 = Cat('cat', 'Gatsby', '2018-07-08') 
pet3 = Dog('dog', 'Toby', '2018-07-08', 'bull dog') 
pet4 = Dog('dog', 'Max', '2018-07-08', 'Tibetan Mastiff') 
print(pet1.name) 
print(pet2.name, "is a chubby", pet2.pet_type) 
pet2.details() 
print(pet3.name, "is a",pet3.breed, "and it always",pet3.sounds("growls")) 
pet4.details() 
'''Write a python program to demonstrate Multiple Inheritance 
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
print("The Modulous of two number(a%b)= ",c.mod(a,b)) '''
