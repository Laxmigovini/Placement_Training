'''
#Basic Level

#Find the largest element in an array.
#Example: Input = [2, 7, 1, 9, 5] → Output = 9
arr = [2, 7, 1, 9, 5]
maxi = 0
for i in range(len(arr)-1):
    if arr[i] > maxi:
        maxi = arr[i]
print(maxi)

#Find the sum of all elements in an array.
#Example: Input = [3, 5, 7] → Output = 15
arr = [3, 5, 7]
s = 0
for i in range(len(arr)):
    s += arr[i]
print(s)

#Reverse an array without using extra space.
#Example: Input = [1, 2, 3, 4] → Output = [4, 3, 2, 1]
arr = [1, 2, 3, 4]
lst = []
for i in range(len(arr)-1,-1,-1):
    lst.append(arr[i])
print(lst)
#or
n = len(arr)
for i in range(n//2):
    arr[i],arr[n-i-1] = arr[n-i-1],arr[i]
print(arr)

#Count the number of even and odd elements in an array.Example: Input = [2, 5, 7, 8, 10] → Output = Even=3, Odd=2
arr = [2, 5, 7, 8, 10]
evenc = 0
oddc = 0
for i in range(len(arr)):
    if arr[i] % 2 == 0:
        evenc+=1
    else:
        oddc+=1
print(evenc,oddc)

#Find the second largest element in an array.Example: Input = [12, 35, 1, 10, 34, 1] → Output = 34
arr = [12, 35, 1, 10, 34, 1]
max1 = 0
max2 = 0
for i in range(len(arr)):
    if arr[i]>max1:
        max2 = max1
        max1 = arr[i]
    if max2 < arr[i] and arr[i] != max1:
        max2 = arr[i]
print(max2)

#Rotate an array by k positions (cyclic shift).Example: Input = [1, 2, 3, 4, 5], k=2 → Output = [4, 5, 1, 2, 3]
arr = [1, 2, 3, 4, 5]
k = 2
k = k%len(arr)
rotated = arr[-k:]+arr[:-k]
print(rotated)
#or

def reverse(arr,s,e):
    while s<e:
        arr[s],arr[e] = arr[e],arr[s]
        s+=1
        e-=1
def rotate(arr,k):
    n = len(arr)
    k = k%n
    reverse(arr,0,n-1)
    reverse(arr,0,k-1)
    reverse(arr,k,n-1)
    return arr
print(rotate(arr,2))


#Check if an array is a palindrome.Example: [1, 2, 3, 2, 1] → Yes
arr = [1, 2, 3, 2, 1]
if arr == arr[::-1]:
    print("yes")
else:
    print("no")

def ispalindrome(arr):
    left = 0
    right = len(arr)-1
    while left < right:
        if arr[left] != arr[right]:
            return False
        left+=1
        right-=1
    return True
print(ispalindrome(arr))

#Find the frequency of each element in an array.Example: Input = [1, 2, 2, 3, 1] → Output: {1:2, 2:2, 3:1}
arr = [1, 2, 2, 3, 1]
freq={}
for i in arr:
    if i in freq:
        freq[i]+=1
    else:
        freq[i] = 1
print(freq)
'''

#Find two numbers that add up to a target value.Example: Input = [2, 7, 11, 15], target = 9 → Output = (2, 7)
arr = [2,7,11,15]
target = 9
freq={}
for i,num in enumerate(arr):
    compliment = target - arr[i]
    if compliment in freq:
        print(freq[compliment],arr[i])
        break
    freq[num] = arr[i]

#Find the maximum subarray sum (Kadane’s Algorithm).Example: Input = [-2, 1, -3, 4, -1, 2, 1, -5, 4] → Output = 6
#(Subarray: [4, -1, 2, 1])
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
