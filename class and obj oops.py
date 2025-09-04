
class areaofcircle:
    r=int(input("enter r value:"))
    a=3.14*r*r
class areaoftriangle:
    b=int(input("enter b value:"))
    h=int(input("enter h value:"))
    t=0.5*b*h
    def read(self): 
        print("Reading") 
        print("Instance Object:",self.areaoftriangle) 
    def write(self): 
        print("Writing") 
#creation of object: 
s1 = areaofcircle()
s1=areaoftriangle()
print("area of circle:",s1.areaofcircle) 
print("areaof triangle:",s1.areaoftriangle) 
s1.read() 
s1.write() 
