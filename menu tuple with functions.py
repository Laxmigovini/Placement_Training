t=()
t1=()
n=int(input())
for i in range(n):
    t1=int(input())
    t+=(t1,)
print(t)
def maximum(t1):
    m=max(t1)
    return m
def minimum(t1):
    mi=min(t1)
    return mi
def average(t1,num):
    avg=sum(t1)/num
    return avg
def sortas(t1):
    print("elements in ascending order:",sorted(t1))
def sortdes(t1):
    print("elements in descending order:",sorted(t1,reverse=True))
print("1.maximum")
print("2.minimum")
print("3.average")
print("4.sort-ascending")
print("5.sort-descending")
print("6.exit")
print("enter your choice:")
c=int(input())
if(c==1):
    ma=maximum(t)
    print("maximum of element in tuple:",ma)
elif (c==2):
    min=minimum(t)
    print("minimum of elements in tuple:",min)
elif(c==3):
    a=average(t,n)
    print("average of elements in tuple:",a)
elif(c==4):
    sortas(t)
elif(c==5):
    sortdes(t)
else:
    print("end program")
