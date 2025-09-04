a = [13,14,2,5,18,1,4]
max_profit = 0
for i in range(6): #i is buying . we can buy from monday to saturday
    for j in range(i+1,7): # j is selling. we can sell from tuesday to sunday
        profit = a[j] - a[i]
        max_profit = max(max_profit,profit)
print(max_profit)