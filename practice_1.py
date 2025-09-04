'''
def is_prime(n,i=2):
    
    if n == 2 or n == 3:
        return True
    if n <= 1:
        return False
    if n % i == 0:
        return False
    if i*i>n:
        return True
    return is_prime(n,i+1)

def check_prime(n):
    if is_prime(n) == True:
        print("it is prime")
        if n > 200:
            print("it is greater than 200")
        else:
            print("it is not greater than 200")
    else:
        print("it is not prime")

n = int(input())
check_prime(n)


n = int(input())
i = 2

if n<=1:
    print("not prime")
if n == 2 or n == 3:
    print("prime")
else:
    is_prime = True
    for i in range(2, n//2+1):
        if n % 2 == 0:
            is_prime = False
            break
    if is_prime == True:
        print("prime")
    else:
        print("not prime")



a = [2,3,5,4,5,3,2,4,6,7,8,7,8]
listt = dict()
for i in a:
    if i in listt:
        listt[i]+=1
    else:
        listt[i] = 1
    
for key,value in listt.items():
    if value == 1:
        print(key)

a = [2,3,5,4,5,3,2,4,6,7,8,7,8]

for i in range(len(a)):
    count = 0
    for j in range(len(a)):
        if a[i] == a[j]:
            count += 1
    if count == 1:
        
        print(a[i])


a = [2,2,3,3,4,5,5,6,6]
n = len(a)
for i in range(0,n-1,2):
    if a[i] == a[i+1]:
        i = i+2
    else:
        print(a[i])
        break
else:
    print(a[-1])

'''

a = [1,2,3,4,5,6,7,8,9]
maxx = 1
hmaxx = 1
for i in range(len(a)-1):
    if a[i]-a[i+1] == -1:
        maxx+=1
    else:
        hmaxx = max(hmaxx,maxx)
        maxx = 1
hmaxx = max(hmaxx,maxx)
print(hmaxx)





















