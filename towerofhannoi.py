def towerofhannoi(n:int,a:int,b:int,c:int)->int:
    if n>0:
        towerofhannoi(n-1,a,c,b)
        print("%d%d"%(a,c))
        towerofhannoi(n-1,b,a,c)
n=int(input("enter number of discs:"))
towerofhannoi(n,1,2,3)
                      
