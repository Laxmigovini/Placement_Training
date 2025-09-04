n = int(input())
number = n 
rev = 0
while n != 0:
    num = n % 10
    rev = rev * 10 + num
    n = n // 10
if rev == number:
    print("palindrome")
else:
    print("not palindrome")