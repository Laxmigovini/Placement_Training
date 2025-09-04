nums = [2,3,1,1,4]
def canjump(nums):
    maxx = 0
    for i in range(len(nums)):
        if i > maxx:
            return False
        maxx = max(maxx,nums[i]+i)
    return True
print(canjump(nums))