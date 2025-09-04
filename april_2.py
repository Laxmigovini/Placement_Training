'''
def joseph_problem(n,k):
    queue = list(range(1, n + 1))
    index = 0
    while len(queue) > 1:
        index = (index + k - 1) % len(queue)
        queue.pop(index)   #eliminate every second position person
    return queue[0]
n = int(input())
k = int(input())
print(joseph_problem(n,k))


#REverse a queue using stack
'''


class Queue:
    def __init__(self):
        self.items = []
        self.front = None
        self.rear = None
    
    def is_empty(self):
        return len(self.items) == 0
    
    def Dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return
        return self.items.pop(0)
    
    def enqueue(self, element):
        self.items.append(element)
    
    def reverse_queue(self):
        stack = []
        while not self.is_empty():
            stack.append(self.Dequeue())
        while stack:
            self.enqueue(stack.pop())

q = Queue()
print("Enter 5 numbers:")
for _ in range(5):
    num = int(input())
    q.enqueue(num)

print("Original queue:", q.items)
q.reverse_queue()
print("Reversed queue:", q.items)


'''
ALGORITHM:
Step1:initialise an empty stack s
Step2:transfer elements from the queue to the stack
        while the queue Q is not empty
            element=dequeue(Q)
            push(element) into stack s
Step3:reverse the queue by transferring elements back
      while the stack s is not empty
          element = pop(5)
          enqueue(element) into queue Q
Step4:return the reversed queue Q

CODE:
    
def reverse_queue(q):
    stack = []
    while q:
        element = q.pop(0)  
        stack.append(element)  
    while stack:
        element = stack.pop() 
        q.append(element)      
    return q
my_queue = [1, 2, 3, 4, 5]
reversed_queue = reverse_queue(my_queue)
print("Reversed Queue:", reversed_queue)

  '''  


