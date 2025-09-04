n = int(input())
def is_prime(n):
    temp = 0
    for i in range(2,n//2+1):
        if n % i== 0:
            temp = 1
            break
        if temp == 1 or n == 1:
            return False
        return True

if is_prime(n) == True:
    print("it is prime")
    if n > 200:
        print("it is greater than 200")
    else:
        print("it is not greater than 200")
else:
    print("it is not prime")
