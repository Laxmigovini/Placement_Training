import math 
def general_fun(): 
    print(math.sqrt(4)) 
    print(math.ceil(2.5)) 
    print(math.pow(2,5)) 
    print(math.floor(2.5)) 
def fact_fun(): 
    print(math.factorial(4)) 
def sin_fun(): 
    print(math.sin(math.radians(30))) 
def cos_fun(): 
    print(math.cos(math.radians(30))) 
def tan_fun(): 
    print(math.tan(math.radians(30))) 
 
print("press 1: square root, ceil,floor,pow") 
print("press 2: factorial") 
print("press 3: sin") 
print("press 4 : cos") 
print("press 5: tan") 
print("press 6: exit")     
while(input("do you continue[y/n]:")=='y'): 
    choice = int(input("Enter Your choice:")) 
    if choice == 1: 
        general_fun() 
    elif choice == 2: 
        fact_fun() 
    elif choice == 3: 
        sin_fun() 
    elif choice == 4: 
        cos_fun() 
    elif choice == 5: 
        tan_fun() 
    elif choice == 6: 
        quit() 
    else: 
        print("Enter Correct Choice:") 
else: 
    exit()   
