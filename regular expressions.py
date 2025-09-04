import re 
result = re.match('python', 'python programming and python') 
print('Starting position of the match:',result.start()) 
print('Ending position of the match :',result.end()) 
txt = "Welcome to SRU" 
x = re.findall("SRU",txt) 
if x: 
    print("Found") 
else: 
    print("not found") 
#findall() 
import re 
txt = "Welcome to S R University" 
x = re.findall("S R",txt) 
print(x) 
#search(): 
import re 
txt = "Welcome to S R University" 
x = re.search("Welcome",txt) 
if x: 
    print("String is found") 
else: 
    print("String is not found") 
#split() 
import re 
txt = "Welcome to S R University"
x = re.split("\s",txt,2) 
print(x) 
#sub() 
import re 
txt = "Welcome to S R University" 
x = re.sub("\s","sru",txt,2) 
print(x) 
