# DP - fibonacci series 
'''def fibonacci(n):
    arr = [-1] * (n+1)
    if n == 1 or n == 2:
        return 1
    arr[1],arr[2] = 1,1
    for i in range(3,len(arr)):
        arr[i] = arr[i-1] + arr[i-2]
    return arr[i]
print(fibonacci(6))
 ''' 

#memorization - fibonacci series
'''n = 7
dp = [-1]* n
def fibonacci(n):
    if dp[n-1] != -1:
        return dp[n-1]
    if n == 0:
        return 0
    if n == 1:
        return 1
    dp[n-1] = fibonacci(n-1) + fibonacci(n-2)
    return dp[n-1]
print(fibonacci(n))
print(dp)
'''
#frog jump
#min energy required to reach the end - frog can make 1 or 2 jumps
arr = [10,20,30,10,30,20,10]
n = len(arr)
dp = [-1] * n
dp[0] = 0
dp[1] = dp[0] + abs(arr[1]-arr[0])
for i in range(2,n):
    one = dp[i-1] + abs(arr[i]-arr[i-1])
    two = dp[i-2] + abs(arr[i]-arr[i-2])
    dp[i] = min(one,two)
print(dp)

# recursion code
'''arr = [10,20,30,10]
def frogJump(arr,n):
    if n == 0:
        return 0
    if n == 1:
        return abs(arr[1]-arr[0])
    return min(frogJump(arr,n-1) + abs(arr[n]-arr[n-1]), frogJump(arr,n-2) + abs(arr[n]-arr[n-2]))
print(frogJump(arr,len(arr)-1))'''


#memorization
'''arr = [10,20,30,10,30,20,10]
dp = [0,abs(arr[1]-arr[0]),0,0,0,0,0]
def frogJump(arr,n):
    if n <= 1:
        return dp[n]
    dp[n] = min(frogJump(arr,n-1) + abs(arr[n]-arr[n-1]), frogJump(arr,n-2) + abs(arr[n]-arr[n-2]))
    return dp[n]
print(frogJump(arr,6))'''

'''arr = [10,20,30,10]
n = len(arr)
one = 0
two = abs(arr[1]-arr[0])
for i in range(2,n):
    ans = min(one,two)
    two = ans + abs(arr[i]-arr[i-2])
    one = two + abs(arr[i]-arr[i-1])
print(ans)'''

# for k jumps
'''arr = [10,20,30,10,30,20,10]
n = len(arr)
dp =[9999] * n
k = 2
dp[1] = abs(arr[1]-arr[0])
for i in range(n):
    for j in range(1,k+1):
        tem = dp[i-j] + abs(arr[i]-arr[i-j])
        dp[i] = min(dp[i],tem)
print(dp)'''


'''s = [(1,3),(2,5),(4,6),(6,7),(5,8),(7,9)]
pr = [5,6,5,4,11,2]
dp = pr.copy()
for j in range(1,len(pr)):
    for i in range(0,j):
        if s[j][0] >= s[i][1]:
            dp[j] = max(dp[i]+pr[j],dp[j])
print(dp)
'''


arr = [2,3,4,5] 
target = 12
dp = [[0]*(target+1) for j in range(len(arr))]
for i in range(len(arr)):
    dp[i][0] = 1
dp[0][arr[0]] = 1
for i in range(1,len(arr)):
    for j in range(1,target+1):
        if dp[i-1][j-arr[i]] == 1:
            dp[i][j]=dp[i-1][j-arr[i]]
        if dp[i-1][j] == 1:
            dp[i][j] = dp[i-1][j]
        if j < arr[i]:
            dp[i][j] = dp[i-1][j]
for i in dp:
    print(i)
