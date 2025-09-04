'''
a = "15,-3,+,6,2,-,*"
s = []
lst = a.split(',')
for i in lst:
    if i[-1].isdigit():
        s.append(int(i))
    else:
        a1 = s.pop()
        a2 = s.pop()
    if i == "+":
        s.append(a2+a1)
    elif i == "-":
        s.append(a2-a1)
    elif i == "*":
        s.append(a2*a1)
print(s[-1])
'''

class node:
    def __init__(self,u):
        self.data = u
        self.left = None
        self.right = None
    def inorder(self,root):
        if root == None:
            return
        self.inorder(root.left)
        print(root.data,end = " ")
        self.inorder(root.right)
    def preorder(self,root):
        if root == None:
            return
        print(root.data,end = " ")
        self.preorder(root.left)
        self.preorder(root.right)
    def postorder(self,root):
        if root == None:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.data,end = " ")
    def sum_all(self,root):
        s = 0
        if root == None:
            return 0
        return root.data + self.sum_all(root.left)+self.sum_all(root.right)
    def sum_even(self,root):
        if root == None:
            return 0
        if root.data % 2 == 0:
            return root.data + self.sum_even(root.left)+self.sum_even(root.right)
        return self.sum_even(root.left)+self.sum_even(root.right)
    def height_tree(self,root):
        if root == None:
            return -1
        return max(self.height_tree(root.left),self.height_tree(root.right))+1
    def search_ele(self,root,n):
        if root == None:
            return "not found"
        if root.data == n:
            return "found"
        if root.data < n:
            return self.search_ele(root.right,n)
        if root.data > n:
            return self.search_ele(root.left,n)
            
        
        
root = node(10)
root.left = node(5)
root.right = node(20)
root.left.left = node(2)
root.left.right = node(8)

root.inorder(root)
print()
root.preorder(root)
print()
root.postorder(root)
print()
print(root.sum_all(root))
print()
print(root.sum_even(root))
print()
print(root.height_tree(root))
print()
print(root.search_ele(root,2))
