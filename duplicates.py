
listt = [2,3,4,3,2,5,5]
#every number has freequency of 2 except 1 number. print that number
list1 = dict()
for i in listt:
    if i in list1:
        list1+=1
    else:
        list1 = 1
for key,value in list1.item():
    if value==1:
        print(key)