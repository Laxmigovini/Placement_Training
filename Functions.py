'''
#FUNCTIONS
def fun():
    print("Hello All")
fun()
fun()

def fun(Name):
    print("Hello",Name)
fun("Python")
#POSITIONAL ARGUMENTS
def add(a,b):
    print(a+b)
add(5,10)

#KEY ARGUMENTS
def greet(name,CGPA):
    print(f"My Name is: {name}, My CGPA: {CGPA}")
greet(name="Laxmi",CGPA=9.37)
greet(CGPA=9.37,name="govini")

#DEFAULT ARGUMENTS
def greet(name,CGPA=9.3):
    print(f"My Name is: {name}, My CGPA: {CGPA}")
greet(name="Rohan")
greet(name="Nani",CGPA=8.5)

#VARIABLE LENGTH ARGUMENTS
def greet(*names):
    for name in names:
        print(f"Hello {name}")
greet("Rohan", "Nani", "Charlie")


def largest_of_three(a,b,c):
    if (a>b and a>c):
        return a
    elif(b>a and b >c):
        return b
    else:
        return c
a=int(input())
b=int(input())
c=int(input())
print(largest_of_three(a,b,c))

def reverse_string(name):
    name=name[::-1]
    print(name)
name=input()
reverse_string(name)

def even_odd(num):
    if(num%2==0):
        print("even")
    else:
        print("odd")
num=int(input())
even_odd(num)

def factorial(string):
    if(string==string[::-1]):
        print("palindrome")
    else:
        print("not palindrome")
string=input()
factorial(string)    

def fact(num):
    if num==0:
        return 1
    else :
        return num * fact(num-1)
num=int(input())
print(fact(num))

def even_num():
    sum = 0
    for i in range(1,11):
        if i %2==0:
            sum+=i
    return sum
print(even_num())

def sum_even(list1):
    return sum( num for num in list1 if num%2==0)
list1=[1,2,3,4,5,6,7,8,9]
print(sum_even(list1))

def longest_string(list):
    return max(list,key=len)
strings=["apple","banana","apple"]
print("Longest string:",longest_string(strings))

#INTERSECTION OF 2 STRINGS
str1=["apple","banana"]
str2=["banana"]
str1=set(str1)
str2=set(str2)
print(str1 and str2)

#INTERSECTION OF 2 LISTS
list1=[1,2,3,4,5]
list2=[4,5,6,7,8]
list1=set(list1)
list2=set(list2)
print(list(list1) and list(list2))

#MERGE 2 LISTS INTO ONE
list1=[1,2,3,4,5]
list2=[4,5,6,7,8]
list1=set(list1)
list2=set(list2)
print(list1 | list2)

def divisible_list(list1,n):
    lis = []
    for num in list1:
        if num % n ==0:
            lis.append(num)
    return lis
            
list1=[1,2,3,4,5]
n=2
print(divisible_list(list1,n))

def sum_of_squares(list1):
        return [i**2 for i in list1]
list1=[1,2,34,5,6,7]
print(sum_of_squares(list1))


def frequency_char(string):
    char_freq={}
    for char in string:
        if char in char_freq:
            char_freq[char]+=1
        else:
            char_freq[char]=1
    return char_freq
string=input()
print(frequency_char(string.lower()))
 
def max_diff_btwtwoelements(list1):
    max_value=0
    for i in range(len(list1)):
        for j in range(i+1,len(list1)):
            if abs(list1[i]-list1[j])>max_value:
                max_value=abs(list1[i]-list1[j])
    return max_value
list1=[1,3,5,8,6,78,9]
print(max_diff_btwtwoelements(list1))
 
def words_longer_than(text,n):
    words=text.split()
    return len([word for word in words if len(word)>n])
text="The quick brown fox jumps over the lazy dog"
n=int(input())
print(words_longer_than(text,n))



def divisible_by_3or5(n):
    return [i for i in range(1,n+1) if i%3==0 or i %5==0]
            
n =int(input())
print(divisible_by_3or5(n))

def ele_greater_than_n(n):
    return [i for i in list1 if i >n]
list1=[1,23,3,45,67,76]
n=int(input())
print(ele_greater_than_n(n))

def anagrams(s1,s2):
    s1=sorted(s1)
    s2=sorted(s2)
    if s1==s2:
        print("anagram")
    else:
        print("not an anagram")
s1=input()
s2=input()
anagrams(s1,s2)

def duplicates_withoutbuiltordict(list1):
    output_list=[]
    for i in list1:
        if i not in output_list:
            output_list.append(i)
    return output_list
list1=[1,2,3,4,5,2,5,6,2]
print(duplicates_withoutbuiltordict(list1))
'''
def rotation_ofstring():
    s1=input()
    s2=input()
    s=s1+s1
    return s2 in s1+s1
print(rotation_ofstring())


     
    
            
            
    




















