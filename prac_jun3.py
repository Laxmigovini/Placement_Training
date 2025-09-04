'''arr = [2,3,4,5]
target = 12
dp = [[0]*(target+1) for i in range(len(arr))]
for i in range(len(arr)):
    dp[i][0]=1
dp[0][arr[0]]=1
for i in range(1,len(arr)):
    for j in range(1,target+1):
        if j<arr[i]:
            dp[i][j] = dp[i-1][j]
        else:
            if dp[i-1][j]==1:
                dp[i][j] = dp[i-1][j]
            else:
                if dp[i-1][j-arr[i]]==1:
                    dp[i][j] = dp[i-1][j-arr[i]]
                else:
                    dp[i][j] = 0
for i in dp:
    print(i)
if dp[-1][-1] == 1:
    print("possible")
else:
    print("not possible")

               
arr = [2,3,4,5]
target = 12
dp = [[0]*(target+1) for i in range(len(arr))]
for i in range(len(arr)):
    dp[i][0]=0
dp[0][arr[0]]=1
for i in range(1,len(arr)):
    for j in range(1,target+1):
        if j < arr[i]:
            dp[i][j] = dp[i-1][j]
        else:
            if arr[i] == j:
                dp[i][j] = 1
            elif dp[i-1][j-arr[i]]>=1:
                dp[i][j] = dp[i-1][j-arr[i]]+1
            elif dp[i-1][j]>1:
                dp[i][j]=min(dp[i-1][j],1+dp[i-1][j])    
for i in dp:
    print(i)

'''















