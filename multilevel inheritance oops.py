#Base class 
class Grandfather: 
    def speak(self): 
        print("My Grand father speakes true.") 
    def color(self): 
        print("My Grand Father color is white.") 
    def thought(self): 
        print("My Grand father behaviour is simple and cool") 
#derived or child class 1 
class Father(Grandfather): 
     def education(self): 
         print("My Father is a Farmer") 
#derived or child class 2 
class son(Father): 
    def grade(self): 
        print("My daughter is in 7th Grade in CAIE.") 
#creating the object of child class 
s=son() 
s.thought() 
s.color() 
s.education() 
s.grade() 
