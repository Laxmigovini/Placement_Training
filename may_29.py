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
    def insert(self,root,x):
        if root == None:
            return node(x)
        if x < root.data:
            root.left = self.insert(root.left,x)
        else:
            root.right = self.insert(root.right,x)
        return root
    def count_leaf_nodes(self,root):
        if root == None:
            return 0
        if root.left is None and root.right is None:
            return 1
        return self.count_leaf_nodes(root.left)+ self.count_leaf_nodes(root.right)
    def print_path(self,root,listt=[]):
        if root == None:
            return 
        if root.left is None and root.right is None:
            print(listt+[root.data])
        self.print_path(root.left,listt+[root.data])
        self.print_path(root.right,listt+[root.data])
    def path(self,root,l):
        if root == None:
            return
        l.append(root.data)
        if root.left is None and root.right is None:
            print(l)
            l.pop()
            return
        self.path(root.left,l)
        self.path(root.right,l)
        l.pop()
    
    def Balanced(self, root):
        def check(node):
            if node is None:
                return -1
            left = check(node.left)
            #if left == -1:
             #   return -1
            right = check(node.right)
            #if right == -1:
              #  return -1
            if abs(left - right) > 1:
                return -1
            return max(left, right) + 1

        if check(root) == -1:
            print("Not Balanced")
        else:
            print("Balanced")

    def level_order_traversal(self,root,l):
        if root == None:
            return
        l.append(root)
        while l:
            curr = l.pop(0)
            if curr.left != None:
                l.append(curr.left)
            if curr.right != None:
                l.append(curr.right)
            print(curr.data,end = ' ')
    def check_leaf_levelorder(self,root,l):
        if root == None:
            return
        l.append(root)
        c = 0
        while l:
            #f = 0
            curr = l.pop(0)
            if curr.left == None and curr.right == None:
                c+=1
            if curr.left != None:
                l.append(curr.left)
                f = 1
            if curr.right != None:
                l.append(curr.right)
                f = 1
            #if f == 1:
                #c+=1
        return c
    def left_view(self,root,c = 0,freq = {}):
        
        if root == None:
            return
        if c not in freq.keys():
            freq[c] = root.data
            print(freq[c])
        
        self.left_view(root.left,c+1)
        self.left_view(root.right,c+1)
    def right_view(self,root,c=0,freq={}):
        if root == None:
            return
        if c not in freq.keys():
            freq[c] = root.data
        else:
            freq[c] = root.data
            
        self.right_view(root.left,c+1)
        self.right_view(root.right,c+1)
        return freq.values()
    def top_view(self,root,c=0,freq={}):
        if root == None:
            return
        if c not in freq.keys():
            freq[c] = root.data
        else:
            if c > 0:
                freq[c] = root.data
        self.top_view(root.left,c-1)
        self.top_view(root.right,c+1)
        return freq.values()
    def top(self,root):
        c = 0
        listt = [(root,c)]
        d = {}
        while listt:
            curr,c = listt.pop(0)
            if c not in d:
                d[c] = curr.data
            if curr.left != None:
                listt.append((curr.left,c-1))
            if curr.right != None:
                listt.append((curr.right,c+1))
        for i in sorted(d):
            print(d[i],end=' ' )
    def Bottom(self,root):
        c = 0
        listt = [(root,c)]
        d = {}
        while listt:
            curr,c = listt.pop(0)
            d[c] = curr.data
            if curr.left != None:
                listt.append((curr.left,c-1))
            if curr.right != None:
                listt.append((curr.right,c+1))
        for i in sorted(d):
            print(d[i],end=' ' )

    def LCA_BST(self,root,p,q):
        if root == None:
            return
        if p <root.data and q < root.data:
            LCA_BST(root.left,p,q)
        if p > root.data and q > root.data:
            LCA_BST(root.right,p,q)
        return root.data
    def LCA_BT(self,root,p,q):
        if root == None:
            return
        if p == root.data or q == root.data:
            return root
        left = self.LCA_BT(root.left,p,q)
        right = self.LCA_BT(root.right,p,q)
        if left != None and right != None:
            return root.data
        if left != None:
            return left
        else:
            return right
        
        
  
root = node(6)
root.insert(root,3)
root.insert(root,2)
root.insert(root,7)
root.insert(root,5)
root.insert(root,9)
#root.inorder(root)
#print()
#print(root.count_leaf_nodes(root))
#print()
#root.print_path(root)
#root.path(root,[])
root.Balanced(root)
#root.level_order_traversal(root,[])
#print(root.check_leaf_levelorder(root,[]))
#root.left_view(root)
#print(root.right_view(root))
#print(root.top_view(root))
#root.top(root)
#root.Bottom(root)
#print(root.LCA_BST(root,2,9))
#print(root.LCA_BT(root,2,9))
