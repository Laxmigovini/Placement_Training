'''
#SET
s1={1,2,3,4,5}
print(s1)
#ADD
s1.add(7)
print(s1)
#CLEAR
s1.clear()
print(s1)

s1={1,2,3,4,5,7,6,7,9}
#COPY
s2=s1.copy()
print(s2)
print(s1)

#DIFFERENCE
s1={1,2,3,4,5}
s2={4,5,6,7,8}
print(s1-s2)
print(s1.difference(s2))


#REMOVE
s1={1,2,3,4,5}
s1.remove(3)
print(s1)
s1.remove(10)
print(s1)#key errors

#DISCARD
s1={1,2,3,4,5}
s1.discard(3)
print(s1)
s1.discard(10)
print(s1)

#INTERSECTION
s1={1,2,3,4,5}
s2={4,5,6,7,8}
s3=s1.intersection(s2)
print(s3)

#UNION
s1={1,2,3,4,5}
s2={4,5,6,7,8}
s3=s1.union(s2)
print(s3)

#POP
s1={1,2,3,4,5,1,2,3}
s1.pop()
print(s1)

#SYMMETRIC_DIFFERENCE_UPDATE
s1={1,2,3,4,5}
s2={4,5,6,7,8,9}
s1.symmetric_difference_update(s2)
print(s1)
'''
a=[1,2,3,4,5]
print(type(a))
a=tuple(a)
print(type(a))
a=set(a)
print(type(a))









