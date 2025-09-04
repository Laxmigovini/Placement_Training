d=list(map(int ,input().split()))
data1=d.sort()
n=len(data1)
def median(data1:list[int],length:int)->float:
    if n%2==0:
        median1=data1[n/2]
        median2=data1[n/2-1]
        median=(median1+median2)/2
    else:
        median=data1[n/2]
    return median
def mode(data1:list[int],length:int)->float:
    mod_arr={}
    for i in data1:
        mod_arr.append(data1.count(i))
    return max(mod_arr)
d=list(map(int ,input().split()))
n=len(data1)
medi=median(data1,n)
mod=mode(data1,n)
print("median of given data:",medi)
print("mode of given data:",mod)
