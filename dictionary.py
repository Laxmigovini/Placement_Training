'''
d1={"Name":"Laxmi","ID":312}
print(d1)
print(type(d1))

#UPGRADING THE VALUE
d1={"Name":"Laxmi","ID":312,"Name":"govini"}
print(d1)
print(type(d1))

#CLEAR
d1={"Name":"Laxmi","ID":312,"Name":"govini"}
d2={"Name":"Laxmi","ID":312}
d1.clear()
print(d1)

#COPY
d1={"Name":"Laxmi","ID":312,"Name":"govini"}
d2={"Name":"Laxmi","ID":312}
d3=d2.copy()
print(d3)

d1={"Name":"Laxmi","ID":312,"Name":"govini"}
print(d1.items())
print(d1.keys())
print(d1.values())
print(d1.get("Name"))

#UPDATE
d1={"Name":"Laxmi","ID":432}
d1["Location"]="HNK"
d1.update({"a":100})
print(d1)
#POP
d1={"Name":"Laxmi","ID":432}
d1.pop("Name")
print(d1)
#POPITEM
d1={"Name":"Laxmi","ID":432}
d1.popitem()
print(d1)

d1={"a":1,"b":2,"c":3}
print("a" in d1)
print("a" not in d1)
'''
#square of a tuple
t1=(1,2,3,4,5,6,7,8,9,98,76)
print(tuple(i**2 for i in t1))











