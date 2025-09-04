'''
t1=(1,2,1,2,"laxmi")
print(t1)
print(type(t1))

#SUM
t1=(1,2,3)
print(sum(t1))

#MAX AND MIN
t1=(1,2,3)
print(max(t1))
print(min(t1))

#COUNT
t1=(1,2,1,2,"laxmi")
print(t1.count(1))

#SORTED()
t1=(6,3,2,7,5,9,10)
print(sorted(t1))

#REVERSED
t1=(6,3,2,7,5,9,10)
print(tuple(reversed(t1)))

#INDEX
t1=(6,3,2,7,5,9,10)
print(t1.index(3))

#INDEXING
t1=(6,3,2,7,5,9,10)
print(t1[4])

#SLICING
t1=(1,2,3,4,5,6,7,8,9)
print(t1[0:5])

#CONCATENATION
t1=(1,2,3)
t2=(4,5,6,7)
print(t1+t2)

#REPETITION
t1=(1,2,3,4)
t2=[1,2,3,4]
print(t1*3)
print(t2*3)

#CREATE A TUPLE WITH ELEMENTS FROM 1 TO 10 AND FIND THE SUM OF ITS ELEMENTS
t1=[]
for i in range(1,11):
    t1.append(i)
print(tuple(t1))
print(sum(t1))



t1=tuple(range(1,11))
print(t1)
print(sum(t1))

list1=[1,2,2,3,4,5,5,5,6,6,7,7]
list2=[]
for i in list1:
    if i not in list2:
        list2.append(i)
print(list2)


list1=[1,2,2,3,4,5,5,5,6,6,7,7]
number=int(input())
list2=[]
for i in list1:
    if i % number==0:
        list2.append(i)
print(list2)

#COMMON ELEMENTS
list1=[1,2,2,3,4,5,5,5,6,6,7,7]
list2=[1,2,3,4,5,7]
lis=[]
for i in list1:
    if i in list2:
        lis.append(i)
print(lis)

list=["wertyuojjgfdsxcvbn","laxmi","hii","wertyu"]
length=len(list[0])
long_str=list[0]
for string in list:
    if len(string)>length:
        length=len(string)
        long_str=string
print(long_str)
'''
#CHECK IF ELEMENT EXIST IN A TUPLE
t1=(1,2,3,4,5,6,7,8)
num=int(input())
if num in t1:
    print(True)
else:
    print(False)









