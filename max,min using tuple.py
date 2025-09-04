t = tuple()
n = int(input("How many numbers you want to enter?: "))
for i in range(0,n):
    num = int(input())
    t = t +(num,)
print('\nThe numbers in the tuple are:')
print(t)
print("\nThe maximum number is:")
print(max(t))
print("The minimum number is:")
print(min(t))



