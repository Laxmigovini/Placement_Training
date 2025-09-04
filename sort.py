
'''arr = [4,2,5,6,1,2,7,7]
for i in range(len(arr)):
    flag = 0
    for j in range(0,len(arr)-i-1):
        if arr[j] > arr[j+1]:
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp
            flag = 1
    if flag == 0:
        break
print(arr)
           
        
arr = [3,5,2,1,4,8,7,9,3]
k = 2
for i in range(k,len(arr)):
    flag = 0
    for j in range(k,len(arr)-k-1):
        if arr[j] > arr[j+1]:
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp
            flag = 1
    if flag == 0:
        break

print(arr)
            

#arr = [3,5,2,1,4,8,7,9,3]
arr = [4,0,8,22,9,6,1]
k = 2
for i in range(len(arr)):
    flag = 0
    for j in range(0,len(arr)-i-1):
        if arr[j] > arr[j+1]:
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp
            flag = 1
        if i== k:
            print( arr[len(arr)-k])
            break
    if flag == 0:
        break
    

print(arr)

arr = [4,0,8,22,9,6,1]
k = 3
def sort(arr,k):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
            if i == k:
                return arr[len(arr)-k]
        print(arr)
print(sort(arr,k))
  

arr = [4,0,8,22,9,6,1]
k = 2
c=0
for i in range(len(arr)-1):
    for j in range(len(arr)-1-i):
        if arr[j]>arr[j+1] :
            arr[j],arr[j+1] = arr[j+1],arr[j]
            c+=1
    if i == k:
        print(arr[len(arr)-k])

print(c)
           
arr = ['b','a','d','e','c']
for i in range(len(arr)):
    flag = 0
    for j in range(0,len(arr)-i-1):
        if arr[j] > arr[j+1]:
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp
            flag = 1
    if flag == 0:
        break
print(arr)

arr = [[2,3],[5,1],[1,4],[2,7],[1,2]]
for i in range(len(arr)):
    flag = 0
    for j in range(0,len(arr)-i-1):
        if arr[j][-1] > arr[j+1][-1]:
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp
            flag = 1
    if flag == 0:
        break
print(arr)


arr = ['hello','car','apples','hi','hey','apple']
for i in range(len(arr)):
    flag = 0
    for j in range(0,len(arr)-i-1):
        for l in range(2):
            if (arr[j][l]) > (arr[j+1][l]):
                arr[j],arr[j+1] = arr[j+1],arr[j]
            
                flag = 1
                break
            elif arr[j][l]<arr[j+1][l]:
                break
            
    if flag == 0:
        break
print(arr)


for i in range(len(arr)):
    for j in range(len(arr)-1-i):
        if arr[j][0] > arr[j+1][0]:
            arr[j],arr[j+1] = arr[j+1],arr[j]
        elif arr[j][0] == arr[j+1][0] and arr[j][1] > arr[j+1][1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]
print(arr)
           

arr = [[4,13,12],[8,10,5],[7,9,20],[14,8,3]]
def is_prime(n,i = 2):
    
    if n == 2 or n == 3:
        return True
    if n <=1:
        return False
    if n % i == 0:
        return False
    if i*i >n:
        return True
    return is_prime(n,i+1)
def prime(lst):
    for i in lst:
        a = is_prime(i)
        if a == True:
            return i
def sort_prime(arr):
    array = []
    for i in range(len(arr)):
        p = prime(arr[i])
        array.append(p)
    print(array)    
    for j in range(len(array)):
        flag = 0
        for k in range(0,len(array)-j-1):
            if array[k] > array[k+1]:
                array[k],array[k+1] = array[k+1],array[k]
                arr[k],arr[k+1]=arr[k+1],arr[k]
                flag = 1
        if flag == 0:
            break
    return arr    
        
print(sort_prime(arr))


words = "an apple a day keeps doctor away"

lis = list(words.split())
listt = []
for i in lis:
    listt.append(len(i))
for j in range(len(listt)):
    flag = 0
    for k in range(0,len(listt)-j-1):
        if listt[k] > listt[k+1]:
            listt[k],listt[k+1] = listt[k+1],listt[k]
            lis[k],lis[k+1]=lis[k+1],lis[k]
            flag = 1
    if flag == 0:
        break
       
        
print(" ".join(lis))

arr = [7,2,6,3,6,7,7,2,2,2]
freq=dict()
for i in arr:
    if i in freq:
        freq[i]+=1
    else:
        freq[i] = 1

value = list(freq.values())
key = list(freq.keys())

for i in range(len(value)-1):
    flag = 0
    for j in range(len(value)-1-i):
        if value[j]>value[j+1]:
            value[j],value[j+1]=value[j+1],value[j]
            key[j],key[j+1] = key[j+1],key[j]
            flag = 1
    if flag == 0:
        break
array = []
for i in key:
    array.extend([i]*freq[i])
    
print(array)


#using bucket sort.
arr = [7,2,6,3,6,7,7,2,2,2]
freq=dict()
for i in arr:
    if i in freq:
        freq[i]+=1
    else:
        freq[i] = 1


#empty_list = [[0]*10]
print(freq)
n = max(freq.values())
bucket=[]
for i in range(n+1):
    bucket.append([])
print(bucket)
for i in freq.items():
    bucket[i[1]].append(i[0])
print(bucket)
listt = []
for i in range(len(bucket)):
    for j in bucket[i]:
        listt.extend([j]*(i))
print(listt)
 '''

def qwe(x):
    for i in x:
        for j in range(2,int(i**0.5)+1):
            if i % j == 0:
                break
        else:
            return i
    return 0
a = [[3,9],[4,2],[5,8,7],[5,7,2,4]]
a.sort(key=qwe,reverse = True)
print(a)
    
























