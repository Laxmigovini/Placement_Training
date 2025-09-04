a = [1,2,3,4,5,6,7,8,9]
l1=[]
l2=[]
l=[]
for num in a:
    if num <= 1:
        l1.append(num)
        continue
    for j in range(2,int(num*0.5)+1):
        if num % 2 == 0:
            l1.append(num)
            break
    else:
        l2.append(num)
l = l2+l1
print(l)
