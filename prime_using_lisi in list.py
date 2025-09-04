a = [[4,13,12],[8,10,5],[7,9,20],[14,8,3]]
def isprime(n):
    if n <= 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
def smallest_prime_in_row(row):
    primes = [x for x in row if isprime(x)]
    return min(primes) if primes else float('inf')

a.sort(key=smallest_prime_in_row)
print(a)