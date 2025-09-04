lower=list(map(int,input().split()))
upper=list(map(int,input().split()))
hrs=list(map(int,input().split()))
def median(x:list[int],y:list[int],z:list[int]):
    n=sum(z)
    cumsum=0
    for i in range(len(x)):
        cumsum+=z[i]
        if cumsum>n/2:
            low=x[i]
            cf=cumsum-z[i]
            f=z[i]
            h=y[i]-x[i]
            median=low+(n/2-cf)*h/f
            break
        return median
def mode(x:list[int],y:list[int],z:list[int]):
    i=y.index(max(y))
    if i==0:
        f1=z[i]
        f2=z[i+1]
        f0=0
        low=x[i]
        h=y[i]-x[i]
        mode=low+((f1-f0)/(2*f1-f0f2))*h
    elif i==len(z)-1:
        f1=z[i]
        f0=z[i-1]
        f2=0
        low=x[i]
        h=y[i]-x[i]
        mode=low+((f1-f0)/(2*f1-f0f2))*h
    else:
        f1=z[i]
        f0=z[i-1]
        f2=z[i+1]
        low=x[i]
        h=y[i]-x[i]
        mode=low+((f1-f0)/(2*f1-f0f2))*h
    return mode
med=median(lower,upper,hrs)
print("median:",med)
mod=median(lower,upper,hrs)
print("median:",mod)
                     
