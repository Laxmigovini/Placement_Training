'''l1=[1,2,3,4,"Hello","Hi"]
print(l1)
print(type(l1))


l2=list(range(0,11))
print(l2)


name="Laxmi"
l1=list(name)
print(l1)


name1="Hello All"
l2=name1.split()
print(l2)


name1="Hello All"
l2=name1.strip()
print(l2)

#INDEX

list1=[1,2,3,4,5,6,7,8,9,10]
print(list1[-1])
#SLICING
aa=[1,2,3,4,5,6,7,8,9,10]
print(aa[0:9:2])
print(aa[2:7:2])
print(aa[:5])
print(aa[5:])
print(aa[3:7])
print(aa[8::2])
print(aa[6:1:-3])


#LIST VS MUTABILITY
aa=[1,2,3,4,5,6,7,8,9,10]
print(aa)
aa[0]=10
aa[1]=20
print(aa)

list1=[1,2,3,4,5,6,7,8,9,10]
for i in list1:
    print(i)

list1=[1,2,3,4,5,6,7,8,9,10]
for i in list1:
    if i %2==0:
        print(i)
for i in list1:
    if i % 2 !=0:
        print(i)

list1=[1,2,3,4,5,6,7,8,9,10]
print(len(list1))


list1=[1,2,3,2,3,2]
print(list1.count(2))
print(list1.count(4))

list1=[1,2,3,4,5,6,7,8,9,10]
print(list1.index(2))
print(list1.index(100))

for i in range(len(list1)):
    if list1[i]%2==0:
        print(list1[i])


#APPEND(): ADD AN ELEMENT AT THE END
list1=[1,2,3,4,5,6,7,8,9,10]
list1.append(11)
print(list1)
list2=[2,4,5,67,8]
list1.append(list2)
print(list1)

#INSERT():
list1=[1,2,3,4,5]
list1.insert(2,22)
print(list1)#[1,2,22,3,4,5]
list1.insert(3,33)
print(list1)
list1.insert(-1,100)#[1,2,22,33,3,4,100,5]
print(list1)

#EXTEND():
list1=[1,2,3,4,5]
list2=[6,7,8,9,10]
list1.extend(list2)
print(list1)
print(list2)
l1=["laxmi","govini"]
l1.extend(["Muthuri"])
print(l1)

#POP():REMOVE THE LAST ITEM OF THE LIST
l1=[1,2,3,4,5]
a1=l1.pop()
b1=l1.pop()
print(l1)
print(a1)
print(b1)

l1=[1,2,3,4,5]
l1.pop()#[1,2,3,4]
l1.pop()#[1,2,3]
print(l1)

#REVERSE
l1=[1,2,3,4,5]
l1.reverse()
print(l1)

#SORT()
l2=[1,9,7,5,8,4,2,3,10]
l2.sort()
print(l2)
l3=["c","a","b","A","C","B"]
l3.sort()
print(l3)

#DESCENDING ORDER
l2=[1,9,7,5,8,4,2,3,10]
l2.sort()
l2.reverse()
print(l2)

#COPY
l2=[1,2,3,4,5]
l3=l2.copy()
print(l3)
print(l2)

#COMPARING
x=[1,2,3]
y=[1,2,3]
print(x==y)
print(x!=y)
#CLEAR
x.clear()
print(x)
#REMOVE
y.remove(3)
print(y)

#REMOVE DUPLICATES FROM A LIST
list1 = [1,2,2,2,3,3,3,4,5,6]
print(set(list1))'''
#REMOVE DUPLICATES USING FOR LOOP
list2 = [1,2,2,2,3,3,3,4,5,6]
list1 = []
for i in list2:
    if i not in list1:
        list1.append(i)
print(list1)

















