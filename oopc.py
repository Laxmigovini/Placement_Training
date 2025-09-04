'''
class Dog:
    def __init__(self, name, breed):
        self.name=name
        self.breed=breed
    def bark(self):
        return f"{self.name} says woof!"
obj=Dog("Buddy","Golden Retriver")
print(obj.bark())#output:Buddy says woof!

class Book:
    def __init__(self,Name,Author,price):
        self.Name=Name
        self.Author=Author
        self.price=price
    def print(self):
        return f"Book Name:{self.Name},Book Author:{self.Author},Book price:{self.price}"
obj1=Book("Python","Laxmi",300)
print(obj1.print())
obj2=Book("C","Govini",500)
print(obj2.print())
obj3=Book("Java","Laxmi",400)
print(obj3.print())

class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display_details(self):
        return f"name:{self.name},marks:{self.marks}"
obj1=Student("Laxmi",345)
print(obj1.display_details())
obj2=Student("Govini",123)
print(obj2.display_details())

class Laptop:
    def __init__(self,brand,model,price=543677):
        self.brand=brand
        self.model=model
        self.price=price
obj=Laptop("Dell","v5")
print(f"Laptop :{obj.brand},model :{obj.model},price={obj.price}")
obj.price=9877654
print(f"Laptop :{obj.brand},model :{obj.model},price={obj.price}")

#COUNT OBJECTS
class Counter:
    count=0
    def __init__(self):
        Counter.count+=1
obj1=Counter()
obj2=Counter()
obj3=Counter()
print(f"Total Objects created:{Counter.count}")

class Example:
    def __init__(self):
        self.public_var="I am Public"
        self._protected_var="I am Protected"
        self.__private_var="I am Private"
    def show_private(self):
        return self.__private_var
obj=Example()
print(obj.public_var)#I am Public
#Protected:Accessible directly(not recomended,conventionally
print(obj._protected_var)
#print(obj._privateVar) This will raise Attribute error
print(obj.show_private())

class Account:
    def __init__(self):
        self.__account_number=None
        self.__balance=0
    def set_values(self):
        self.__account_number=1234
        self.__balance=0
    def get_values(self):
        return f"account_number:{self.__account_number},balance:{self.__balance}"
obj=Account()
obj.set_values()
print(obj.get_values())

#2.ENCAPSULATED BANK ACCOUNT
class BankAccount:
    def __init__(self):
        self.__account_holder=None
        self._balance=0
    def set_values(self,holder,balance):
        self.__account_holder=holder
        self._balance=balance
    def deposit(self,amount):
        if amount>0:
            self._balance+=amount
        else:
            return "not sufficient"
        return self._balance
    def withdraw(self,amount):
        if amount>self._balance:
            return "not sufficient"
        self._balance-=amount
        return self._balance
Account=BankAccount()
Account.set_values("Laxmi",100000)
print(Account.deposit(20000))
print(Account.withdraw(1000))
 
#SINGLE INHERITANCE

class Parent:
    def display(self):
        print("This is parent class")
class Child(Parent):
    def display1(self):
        print("This is child class")
obj=Child()
obj.display()
obj.display1()

#Multi level inheritance
class Grand_Parent:
    def gp(self):
        print("This from Grand Parent")
class Parent(Grand_Parent):
    def display(self):
        print("This is parent class")
class Child(Parent):
    def display1(self):
        print("This is child class")
obj=Child()
obj.display1()
obj.display()
obj.gp()

#multiple
class Parent:
    def display0(self):
        print("This from  Parent")
class Mother:
    def display1(self):
        print("This is Mother class")
class Child(Parent,Mother):
    def display2(self):
        print("This is child class")
obj=Child()
obj.display2()
obj.display1()
obj.display0()

#hirearchial
class Parent:
    def parent(self):
        print("This from  Parent")
class Child1(Parent):
    def c1(self):
        print("This is Child1 class")
class Child2(Parent):
    def c2(self):
        print("This is child2 class")
obj=Child1()
obj.c1()
obj.parent()
obj2=Child2()
obj2.c2()
obj.parent()

#Hybrid Inheritance
class Parent:
    def parent(self):
        print("This is parent")
class Child1(Parent):
    def c1(self):
        print("This is child1 class")
class Child2(Parent):
    def c2(self):
        print("This is child2 class")
class Grand_child(Child1,Child2,Parent):
    def GC(self):
        print("This is from Grand child")
obj=Child1()
obj.c1()
obj.parent()
'''
class LibraryMember:
     def _init_(self, member_id, name):
        self.__member_id = member_id
        self.__name = name
     def borrow(self):
            print(f"{self.__name} has borrowed a book")
     def return_book(self):
                print(f"{self.__name} has returned a book")
class StudentMember(LibraryMember):
     def _init_(self, member_id, name, grade):
          super()._init_(member_id, name)
          self.__grade = grade
     def check_borrowing_limit(self):
               if self._grade == "A" or self._grade == "B":
                    return 5
               elif self._grade == "C" or self._grade == "D":
                    return 3
               else:
                    return None
class FacultyMember(LibraryMember):
     def _init_(self, member_id, name, department):
          super()._init_(member_id, name)
          self.__department = department
     def extended_borrowing_limit(self):
           return 10
obj = StudentMember("123", "John", "A")
obj.borrow()
obj.return_book()
obj.check_borrowing_limit()
obj = FacultyMember("456", "Jane", "Math")
obj.borrow()
obj.return_book()
obj.extended_borrowing_limit()


























    








































