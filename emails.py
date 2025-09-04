
n=int(input("Enter how many email id to enter : "))
t1=()
un = ()
dom = ()
for i in range(n):
    em = input("Enter email id : ")
    t1 = t1 + (em,)
for i in t1:
    a = i.split('@')
    un = un + (a[0],)
    dom = dom + (a[1],)
print("Original Email id's are : " , t1)
print("Username are : " , un)
print("Doman name are : " , dom)
