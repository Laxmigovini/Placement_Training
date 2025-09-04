#dp_fibonacci
'''def fibonacci(n):
    arr = [-1] * (n+1)
    if n == 1 or n == 2:
        return 1
    arr[1],arr[2] = 1,1
    for i in range(3,len(arr)):
        arr[i]=arr[i-1]+arr[i-2]
    return arr[i]
print(fibonacci(5))

#memeoization using dp fibonacci
n = 6
dp = [-1]*n
def fibonacci(n):
    if dp[n-1] != -1:
        return dp[n-1]
    if n == 0:
        return 0
    if n == 1:
        return 1
    dp[n-1]=fibonacci(n-1)+fibonacci(n-2)
    return dp[n-1]
print(fibonacci(n))
print(dp)
'''
arr = [10,20,30,10,30,20,10]
n = len(arr)
dp=[-1]*n
dp[0] = 0
dp[1]=dp[0]+abs(arr[1]-arr[0])
for i in range(2,n):
    one = dp[i-1]+abs(arr[i]-arr[i-1])
    two=dp[i-2]+abs(arr[i]-arr[i-2])
    dp[i]=min(one,two)
print(dp)








