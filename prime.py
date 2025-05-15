n = int(input())
prime = True

def prime_(n):
    temp = 0
    if n == 2 or n == 3:
        return True
    for i in range(2, n//2+1):
        if n % i == 0:
            temp = 1
            break
    if temp == 1 or n == 1:
        return False
    return True
        
    
if prime_(n) == True:
    print("it is prime")
    if n > 200:
        print("it is grater than 200")
    else:
        print("it is not grater than 200")
else:
    print("not a prime")

    
