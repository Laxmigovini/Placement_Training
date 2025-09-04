age=list(map(int,input().split()))
hrs=list(map(int,input().split()))
def median(x:list[int],y:list[int]):
    n=sum(y)
    cumsum=0
    for i in range(len(x)):
        cumsum+=y[i]
        if cumsum>n/2:
            print("median price is:",x[i])
            break
def mode(x:list[int],y:list[int]):
    i=y.index(max(y))
    mode=x[i]
    print("mode of price is:",mode)
median(age,hrs)
mode(age,hrs)
           
