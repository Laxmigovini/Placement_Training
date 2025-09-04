print("enter data:")
d=list(map(float,input().split()))
print("enter the data:")
f=list(map(float,input().split()))
def mean(d,f):
    t_sum=0
    for i,j in zip(d,f):
        t_sum=sum+i*j
    return (t_sum/sum(f))
mean=mean(d,f)
print("mean:",mean)
def v(d,f,mean):
    std=0
    for i,j in zip(d,f):
        std=std+(i-mean)**2*j
    return (std/sum(f))
variance=v(d,f,mean)
print("variance:",variance)
#a=round(variance,4)
#print(a)
#sd=round(a**(1/2),4)
#print("standard deviation:",sd)
         
