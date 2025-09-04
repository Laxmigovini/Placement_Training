'''def qwer(x):
    if x == 6:
        return
    print("hi",x)
    qwer(x+1)
    print("hi",x)
qwer(1)
print("hello")

def qwer(x):
    if x==4:
        return 200
    print(x)
    t = qwer(x+1)
    print(x)
    return t+x
b=qwer(1)
print(b)
'''

'''def fact(x):
    if x == 0:
        return 1
    return x * fact(x-1)
print(fact(5))'''

'''#sum of even in an array
a = [2,5,6,7,2,1,4,3,6]
s=0
n = len(a)
for i in range(n):
    if a[i] % 2 == 0:
        s+=a[i]
print(s)
'''
'''
a = [2,5,6,7,2,1,4,3,6]
def even_sum(a):
    s=0
    for i in a:
        if i % 2 == 0:
            s+=i
    return s
print(even_sum(a))
    '''

'''a = [1,2,3,4,5,6,7,8,4]
def even_sum(a,i=0):
    if i == len(a):
        return 0
    if a[i] % 2 == 0:
        return a[i] + even_sum(a,i+1)
    else:
        return even_sum(a,i+1)
print(even_sum(a))'''

'''#Reverse number
n = 123
def reverse(n,rev=0):
    if n == 0:
        return rev
    return reverse(n // 10, rev*10+ n%10)
print(reverse(n))
'''
'''#prime
def prime(n,i=2):
    if n<=1:
        return False
    if n == 2 or n == 3:
        return True
    if i * i > n:
        return True
    if n % i == 0:
        return False
    return prime(n,i+1)
n = 7
print(prime(n))'''

'''#count prime numbers in a list
a = [13,17,21,23,22,7,29]
def prime(a,i=2):
    if a % i == 0:
        return False
    if i*i > a :
        return True
    if a<=1:
        return False
    return prime(a,i+1)
def count(a,i,c):
    if i == len(a):
        return c
    if prime(a[i]) == True:
        c+=1
    return count(a,i+1,c)
print(count(a,0,0))
'''
'''
def check_sub_poss_by3(n):
    temp = 1
    i = 3
    j = 5
    while 1:
        n -= i
        if n == 1:
            temp = 1
            return True
        elif n < 1:
            return False
    return False
n = 21
print(check_sub_poss_by3(n))
'''
'''
#given an array as input and k element , find the occurances of k.
ip=[2,4,6,3,3,2,6,1,2,3,6,6,5]
def find(ip,k,i=0,c=0):
    if i == len(ip):
        return c
    if ip[i] == k:
        c+=1
    return find(ip,k,i+1,c)
print(find(ip,2))
'''

'''#if freequency of a number is given then we should print that number. 
ip = [2,3,3,4,4,4,5,6,6,6]
def count(ip,k,i=0,c=0):
    if i == len(ip):
        return c
    if ip[i] == k:
        c += 1
    return count(ip,k,i+1,c)
def freequency(ip,f,i=0,listt=[]):
    if i == len(ip):
        return 
    if count(ip,ip[i]) == f and ip[i] not in listt:
        print(ip[i])
        listt.append(ip[i])
    return freequency(ip,f,i+1,listt)
freequency(ip,1)'''

'''#subsets
arr=[1,2,3]
def subsets(arr,i=0,listt=[]):
    if i == len(arr):
        print(listt)
        return
    subsets(arr,i+1,listt+[arr[i]])
    subsets(arr,i+1,listt)
subsets(arr)'''

'''#print even to one side in a listt and odd numbers to right side
a = [1,2,3,4,5,6,7,8]
listt1 = []
list2=[]
for i in range(len(a)):
    if a[i] % 2 == 0:
        listt1.append(a[i])
    else:
        list2.append(a[i])
listt = listt1+list2
print(listt)'''

'''#without using listt concept
a = [1,2,3,4,5,6,7,8]
left = 0
right = len(a) - 1
while left < right:
    if a[left] % 2 == 0:
        left += 1
    elif a[right] % 2 != 0:
        right -=1
    else:
        a[left],a[right] = a[right],a[left]
        left += 1
        right -= 1
print(a)'''

'''#combination sum that is subset_sum should be equal to k
a = [1,2,4,5]
def subset_sum(a,k,listt=[],i=0):
    if i == len(a):
        if k == 0:
            print(listt)
        return 
    if a[i] <= k:
        subset_sum(a,k-a[i],listt+[a[i]],i+1)
    subset_sum(a,k,listt,i+1)
subset_sum(a,6)'''

'''#if sum if possible print list else -1
a=[2,4,6,8]
temp = 0
def possible_sum(a,k,listt=[],i=0):
    global temp
    if i == len(a):
        if k == 0:
            print(listt)
            temp = 1
        return
    if a[i] <= k:
        possible_sum(a,k-a[i],listt+[a[i]],i+1)
    possible_sum(a,k,listt,i+1)
if temp == 0:
    print(-1)
possible_sum(a,13)'''

'''#print maxi even number and min odd num in an array
a=[1,2,3,4,5,6,7,8]
maxi=0
mini=99999
for i in range(len(a)):
    if a[i] % 2 == 0:
        if a[i] > maxi:
            maxi = a[i]
    else:
        if a[i] < mini:
            mini = a[i]
print(maxi,mini)

def find(a,i=0,maxx=0,mini=99999):
    if i == len(a):
        return maxx,mini
    if a[i] % 2 == 0:
        if a[i] > maxx:
            maxx = a[i]
    else:
        if a[i] < mini:
            mini = a[i]
    return find(a,i+1,maxx,mini)
print(find(a))

'''
'''
# to print factors of a number 9
n = 120
for i in range(1,n+1):
    if n % i == 0:
        print(i)

#another logic
n = 5
i = 1
listt=[]
while i * i <= n:
    if n % i == 0:
        listt.append(i)
        if i != n // i:
            listt.append(n//i)
    i+=1
print(listt)
'''
'''
#string reverse
s = "laxmigovini"
print(s[::-1])
print("".join(reversed(s)))'''
'''
s = "laxmigovini"
reverse = " "
for i in s:
    reverse = i + reverse
print(reverse)'''

