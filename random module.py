import random
 #random()
print(random.random())
 #seed(value): First generated system value
random.seed(5)
print(random.random())
 #integer : randint(start,end)
print(random.randint(1,100))
print(random.randint(1,100))
 #float : random()
print(random.random())
 #choice()
list1 = [1,4,2,3]
print(random.choice(list1))
s = "S R University"
print(random.choice(s))
t = (3,2,7,8)
print(random.choice(t))
 #shuffle(): Changing the position of element
list2 = [3,5,7,8,9]
print("First Shuffle")
random.shuffle(list2)
print(list2)
print("Second Shuffle")
random.shuffle(list2)
print(list2)
print("Third Shuffle")
random.shuffle(list2)
print(list2)
 #uniform(start,end)
print(random.uniform(1,10))
print(random.uniform(1,10))
