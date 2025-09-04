l1 = ["read", "write", "repeat","orange"] 
s1 = "S R University" 
 # creating enumerate objects 
obj1 = enumerate(l1) 
obj2 = enumerate(s1) 
print ("Return type:", type(obj1)) 
print (list(enumerate(l1))) 
  # changing start index to 2 from 0
print(list(enumerate(s1,2)))
