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



#if we had infinite number of coins
arr = [2,3,4,5]
target = 12
dp = [[0]*(target+1) for i in range(len(arr))]
for i in range(len(arr)):
    dp[i][0]=1
for i in range(len(arr)):
    for j in range(target+1):
        if j<arr[i]:
            dp[i][j] = dp[i-1][j]
        else:
            if dp[i-1][j]==1:
                dp[i][j] = dp[i-1][j]
            else:
                if dp[i][j-arr[i]]==1:
                    dp[i][j] = dp[i][j-arr[i]]
                else:
                    dp[i][j] = 0
for i in dp:
    print(i)



arr = [2,3,4,5]
target = 12
dp = [[0]*(target+1) for i in range(len(arr))]
for i in range(len(arr)):
    dp[i][0]=1
for i in range(len(arr)):
    for j in range(target+1):
        if j<arr[i]:
            dp[i][j] = dp[i-1][j]
        else:
            if dp[i-1][j]==1:
                dp[i][j] = dp[i-1][j]
            else:
                if dp[i][j-arr[i]]==1:
                    dp[i][j] = dp[i][j-arr[i]]
                else:
                    dp[i][j] = 0
    if dp[i][target]==1:
        print("possible")
        break
for i in dp:
    print(i)


coin=[2,3,4,5]
target=13
#creating dp table with  
dp=[[0]*(target+1) for i in range(len(coin))]

dp[0][coin[0]]=1

for i in range(1,len(coin)):
    for j in range(1,target+1):
        if j<coin[i]:
            dp[i][j] = dp[i-1][j]
        elif coin[i]==j:
            dp[i][j] = 1
        else:
            if dp[i-1][j-coin[i]]!=0 and dp[i-1][j] !=0:
                dp[i][j]=min(1+dp[i-1][j-coin[i]],dp[i-1][j])
            elif dp[i-1][j]!=0:
                dp[i][j] = dp[i-1][j]
            elif dp[i-1][j-coin[i]]!=0:
                dp[i][j]=1+dp[i-1][j-coin[i]]   
for i in dp:
    print(i)

#min coins with infinite coins using 1D
arr = [2,3,4,5]
target = 12
dp = [0]*(target+1)
for i in range(len(arr)):
    for j in range(arr[i],target+1):
        if j == arr[i]:
            dp[j]=1
        if dp[j]!=0 and dp[j-arr[i]] != 0:
            dp[j]=min(dp[j],1+dp[j-arr[i]])
        elif dp[j-arr[i]]!=0:
            dp[j]=dp[j-arr[i]]+1
print(dp)
'''
#length of longest common subsequence

#trie
class node:
    def __init__(self):
        self.data = {}
        self.flag = False
        self.c=0



















