'''
#here input can have unique and duplicate elements.
arr = [2,4,1,5,8,4,7]
#bruteforce
maxx = -1234
minn = -1234
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        profit =arr[j] - arr[i] 
        if profit > maxx:
            maxx = profit
print(maxx)

buying = arr[0]
profit = 0
selling = 0
maxx = -1234
n = len(arr)
for i in range(n):
    if buying[i] > arr[i]:
        buying = arr[i]
    profit = arr[i] - buying
    if profit > maxx:
        maxx = profit

print(maxx)


def find_the_islands(arr,row,cols):
    count = 0
    for i in range(row):
        for j in range(cols):
            if arr[i][j] == 1:
                if arr[i-1][j]==1 or arr[i][j-1] == 1 or arr[i+1][j]== 1 or arr[i][j+1]==1:
                    count+=1
    return count
arr = [[1,0,0,1,1],[1,0,0,0,1],[0,0,0,1,0],[1,0,0,0,0],[1,0,0,0,1]]
print(find_the_islands(arr,row,cols))

#find the array list elements sum
def find_the_islands(arr,listt,row=5,cols=5):
    lst = []
    for i in range(row):
        row_summ = 0
        for j in range(cols):
            if arr[i][j] == 1:
                row_summ+=arr[i][j]*listt[j]
        lst.append(row_summ)
    return lst
arr = [[0,1,1,0,1],[1,1,0,0,1],[0,0,0,1,1],[0,1,0,0,1],[1,0,0,0,1]]
print(find_the_islands(arr,[8,7,6,5,2]))

#here rat goes only right and bottom.
def rat_toreach_destination(arr,n  ,i=0,j=0 ):
    if i >= n or j >= n or arr[i][j] == 0 :
        return 0
    if i == n-1 and j == n-1 and arr[i][j] == 1:
        return 1
    return rat_toreach_destination(arr,n,i+1,j) + rat_toreach_destination(arr,n,i,j+1)
            
               
arr = [[1,0,0,0,0],[1,1,1,0,0],[1,0,1,0,0],[1,0,1,1,1],[1,1,1,1,1]]
n = 5
print(rat_toreach_destination(arr,n))


def land(arr,i,j,n):
    if i ==n or j == n or i < 0 or j < 0 or arr[i][j] == 0 or arr[i][j] == 2 :
        return 0
    if arr[i][j] == 1:
        arr[i][j] = 2

    land(arr,i-1,j,n)
    land(arr,i,j-1,n)
    land(arr,i,j+1,n)
    land(arr,i+1,j,n)

arr = [[1,0,0,1,1],[1,0,0,0,1],[1,0,0,0,0],[1,0,0,0,0],[1,0,0,0,1]]
for i in arr:
    print(i)

c = 0
for i in range(5):
    for j in range(5):
        if arr[i][j] == 1:
            land(arr,i,j,5)
            c += 1
print(c)

for i in arr:
    print(i)

#single island
c = 0
n = 5
land(arr,0,0,5)
for i in arr:
    print(i)


def burnt_tree(arr,i,j,n):
    if i ==n or j == n or i < 0 or j < 0 or arr[i][j] == 0 or arr[i][j] == 2 :
        return 0
    if arr[i][j] == 1:
        arr[i][j] = 2

    burnt_tree(arr,i-1,j,n)
    burnt_tree(arr,i,j-1,n)
    burnt_tree(arr,i,j+1,n)
    burnt_tree(arr,i+1,j,n)

arr = [[1,0,0,1,1,1],[1,1,1,0,0,0],[0,0,1,1,1,1],[1,1,1,0,0,0],[0,0,0,0,0,1],[1,0,0,1,0,0]]
for i in arr:
    print(i)
c = 0
i = 3
j = 6
n = 6
burnt_tree(arr,i-1,j-1,6)
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            c += 1
print(c)



#single island
c = 0

burnt_tree(arr,2,5,6)
for i in arr:
    print(i)



def frog_jump(n,not_jump,i,j):
    if i ==n or j == n or (i+1,j+1) in not_jump:
        return 0
    if i == n-1 and j == n-1 :
        return 1

    return frog_jump(n,not_jump,i,j+1)+frog_jump(n,not_jump,i+1,j)

not_jump = [(2,1),(4,1),(5,2),(3,5)]
i = 2
j = 3
n = 5
print(frog_jump(n,not_jump,1,2))

import math

def allbinary(a,n,s=''):
    if len(s) == n:
        if int(s,2)<=a:
            print(s)
        return
    allbinary(a,n,s+'0')
    allbinary(a,n,s+'1')

a = 10
n = int(math.log(a,2))+1 # to find length of binary representation.
allbinary(a,n)


import math
def allbinary(a,n,s = ''):
    if a == -1:
        return a
    if len(s) == n:
        print(s)
        a = a-1
        return a
    a = allbinary(a,n,s+'0')
    a = allbinary(a,n,s+'1')

    return a
a = 10
n = int(math.log(a,2))+1 # to find length of binary representation.
allbinary(a,n)
       
import math
def paranthesis(n,s = ''):
    
    if len(s) == n:
        print(s)
        
        return 
    paranthesis(n,s+'(')
    paranthesis(n,s+')')
n = 4
 # to find length of binary representation.
paranthesis(n)
 '''

def paranthesis(n,s='',lc=0,rc=0):
    if len(s) == 2*n:
        print(s)
        return
    
    if lc<rc:
        paranthesis(n,s+'(',lc+1,rc)
    if rc<lc:
        paranthesis(n,s+')',lc,rc+1)
    

n = 3
paranthesis(n)
  













































    
        
