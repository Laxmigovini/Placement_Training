n=["a","e","o","u"]
l=[10,250,30,4,50,6]
n.insert(2,"i")
print(n)
print("l is =",l)
m=l.pop(2)
print(m)
print(l.count(4))
#l.clear()
i=l.index(6)
print(i)
l.sort()
print("After Sorting",l)
k=["n","a","v","a","r","s"]
k.reverse()
print("After Reverse",k)
o=l.copy()
print("After Copying",o)
e=[2,4,6,8]
o=[1,3,5,7]
e.extend(o)
print(e)
