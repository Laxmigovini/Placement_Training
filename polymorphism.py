'''
#POLYMORPHISM
print(10)
print("Hello")
print(10+10)
print("Laxmi"+"Govini")

#METHOD OVERRIDING
class Animal:
    def make_sound(self):
        print("Generic animal sound")
class Dog(Animal):
    def make_sound(self):
        print("woof")
class Cat(Animal):
    def make_sound1(self):
        print("Meow")
animal=Animal()
dog=Dog()
cat=Cat()
animal.make_sound()
dog.make_sound()
cat.make_sound()
print(obj.add(5)
#METHOD OVERLOADING
class Calculator:
    def add(self,a,b=0,c=0):
        return a+b+c
obj=Calculator()
print(obj.add(5))
print(obj.add(5,10))
'''
from multipledispatch import dispatch
class Calculator:
    @dispatch(int,int)
    def add(self,a,b):
        return a+b
    @dispatch(int,int,int)
    def add(self,a,b,c ):
        return a+b+c
calculator = Calculator()
print(calculator.add(10,20))
print(calculator.add(10,13,23))




























