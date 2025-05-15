listt = [2,3,4,3,2,5,5]
#every number has freequency of 2 except 1 number. print that number
list1 = dict()
for i in listt:
    if i in list1:
        list1[i]+=1
    else:
        list1[i] = 1
for key,value in list1.items():
    if value==1:
        print(key)

listt = [2, 3, 4, 3, 2, 5, 5]

unique = 0
for num in listt:
    unique ^= num

print(unique)  # Output: 4



listt = [2,3,4,3,2,5,5]
s=0
for i in listt:
    s=s^i
print(s)


listt = [2,3,4,3,2,5,5]

for i in range(len(listt)-1):
    flag = 0
    for j in range(len(listt)):
        if listt[i] == listt[j] and i!=j:
            flag = 1
            break
    if flag == 0:
        print(listt[i])
            
        
