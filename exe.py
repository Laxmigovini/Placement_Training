print("Laxmigovini")
print(10+10)
#print("Hello"+10)    #Typeerror
#print(10+"Hello")    #Typeerror
print("laxmi"+"govini")
print("laxmi","govini")
print("laxmigovini"*3)
print("laxmi\n"*3)
print("laxmi"+"3")
#print("laxmi"/"3")#Typeerror
name="laxmi"
name='laxmi'

name="""laxmi"""
name='''laxmi'''

print(name)

#comments
Name="""This is python class
This is multiline comment"""
print(Name)

#DATA TYPES
"""1.int
2.float
3.str
4.bool
5.complex"""

#1.int  add 2 numbers
a=10
b=-5
print(a+b)
print(type(a))
print(type(b))

#2. float
c=10.5
d=10
print(c+d)
print(type(c))
e=c+d
print(type(e))

#3. str
a= "laxmi"

 #4. bool
a=10.5 #float
b=5 #int
c="laxmi"
print(c+c)
d=10+5j#complex
print(d)
print(type(d))
e=True #bool
f=False #bool

print(type(e))
print(e+e)
print(e+f)
print(f+f)
print(10+True)

print(d+e)
'''
#GIV EINPUT DYNAMICALLY
a=int(input("enter first number:"))
#b=int(input("enter second number:"))
b=float(input("enter second number:"))
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)


#Student Details
Name=input("Enter Your Name:")
cgpa=float(input("Enter CGPA:"))
Marks=int(input("Enter Marks:"))
print(Name)
print(cgpa)
print(Marks)
print(cgpa+Marks)


#String Value
a=input("enter number")
b=input("enter number")
print(a+b)'''

#TYPE CASTING
#INT
'''a=10
a="laxmi"    #valueerror
b=int(a)
print(type(b))
print(b)
print(type(b))

a="10.5"
b=int(a)
print(type(b))  #value error

a=5+4j
b=int(a)
print(type(b))  #type error


a="5+4j"
b=int(a)
print(type(b))    #value error


#FLOAT

a=10
a=float(a)
print(a)
print(type(a))

a="10.5"
a=float(a)
print(a)
print(type(a))


a="10.5"
a=int(a)
print(a)
print(type(a))    #value error


a="laxmi"
a=float(a)
print(a)
print(type(a))    #value error

a=5+4j
a=float(a)
print(a)
print(type(a))    #type error

a="5+4j"
a=float(a)
print(a)
print(type(a))    #value error



#STR

a=100
a=str(a)
print(a)
print(type(a))




a=True
a=float(a)
print(a)
print(type(a))


#BOOL
a=10
a=bool(a)
print(a)
print(type(a))    #true



a=0
a=bool(a)
print(a)
print(type(a))     #false

a=-1
a=bool(a)
print(a)
print(type(a)) 
a="laxmi"#true
a="@"#true
a=" "#true
a=""#false
a=5+4j #true
a=0+0j #false
b=bool(a)
print(b)
print(type(b))


#COMPLEX

a=100
b=complex(a)
print(b)
print(type(b))

a=-10
b=complex(a)
print(b)
print(type(b))
a="10"
b=complex(a)
print(b)
print(type(b))
a="laxmi"#value error
b=complex(a)
print(b)
print(type(b))
a=10.56
b=complex(a)
print(b)
print(type(b))
a=True
b=complex(a)
print(b)
print(type(b))
a=False
b=complex(a)
print(b)
print(type(b))

a=" "
b=complex(a)
print(b)
print(type(b))   #value error
a=""
b=complex(a)
print(b)
print(type(b)) #value error
a=10
b="2"
print(a+b)    #type error


a=10
b="2"
b=int(b)
print(a+b)

a="10"
b=10
print(a+b)#type error'''

a="4+4j"
a=int(a)
print(a)    #value error












