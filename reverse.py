n = 1234567
rev = 0
while n != 0:
    num = n % 10
    rev = rev * 10 + num
    n = n // 10
print(rev)