'''
s1="Hello All"
print(s1)
print(type(s1))

#LOWER()
s1="Hello All"
print(s1.lower())
print("LAXMI".lower())
print("laxmi".upper())

#LSTRIP():REMOVES THE SPACES OF LEFT SIDE
s1="  Hello All"
print(s1.lstrip())
#RSTRIP()
s1="  Hello All  "
print(s1.rstrip())
#STRIP()
s1="  Hello All  "
print(s1.strip())

#REPLACE():
s1="Hello All"
print(s1)
print(s1.replace("All","Python"))

#SPLIT():
s2="Hello world,Python"
print(s2.split(","))
s2="Hello world Python"
print(s2.split(" "))

#FIND()
s2="Hello world,Python"
print(s2.find("world"))
print(s2.find("l"))

#startswith()
s2="Hello world Python"
print(s2.startswith("H"))
print(s2.startswith("Hello"))
print(s2.startswith("A"))

#endswith()
s2="Hello world Python"
print(s2.endswith("H"))
print(s2.endswith("n"))
print(s2.endswith("A"))

#count()
text="apple Banana apple"
print(text.count("apple"))

#ISALPHA()
text="HelloAll"
print(text.isalpha())
#ISDIGIT()
num="123 "
print(num.isdigit())

#isalnum()
text="Hello123"
print(text.isalnum())
s1="this is python"
print(s1.isspace())

#CAPITALIZE()
s1="this is python"
print(s1.capitalize())
#TITLE()
s2="this is title method"
print(s2.title())

#STRING REVERSAL
s1="Laxmigovini"
print(s1[::-1])

#Palindrome check
s1=input()
if(s1==s1[::-1]):
    print("Palindrome")
else:
    print("not a palindrome")
'''
s1="hello world laxmi hello world govini"
words=s1.split()
w_freq={}
for i in words:
    if i in w_freq:
        w_freq[i]+=1
    else:
        w_freq[i]=1
print(w_freq)







































