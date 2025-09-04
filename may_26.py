class node:
    def __init__(self,data):
        self.data = data
        self.next = None
class linked:
    def __init__(self):
        self.head = None
    def add_back(self,data):
        temp = self.head
        while (temp.next!=None): #keep on moving until next node is not null
            temp = temp.next # keeps moving until it reaches Null
        temp.next = node(data)
    def display(self):
        temp = self.head
        while (temp!=None):
            print(temp.data,end = '->')
            temp = temp.next
        print("None")
    def sum_all(self):
        temp = self.head
        summ = 0
        while temp !=None:
            summ+=temp.data
            temp = temp.next
        print(summ)
    def sum_even(self):
        temp = self.head
        s= 0
        while temp!= None:
            if temp.data % 2 == 0:
                s+=temp.data
            temp = temp.next
        print(s)
    def sum_of_even_pos(self):
        temp = self.head
        s = 0
        i = 1
        while temp!=None:
            if i % 2 == 0:
                s +=temp.data
            i+=1
            temp = temp.next
        print("sum of nodes present at even position:",s)
    def second_largest_num(self):
        temp = self.head
        max1 = -99999
        max2 = -99999
        while temp!=None:
            if temp.data > max1:
                max2 = max1
                max1 = temp.data
            if temp.data > max2 and temp.data!= max1:
                max2 = temp.data
            temp = temp.next
        print(max2)
    def count_consecutive_pair(self):
        temp = self.head
        count = 0
        k = 5
        s= 0
        while temp.next!=None:
            s = temp.data+temp.next.data
            if s<=k:
                count = count+1
            temp=temp.next
        print(count)
    def count_possible_pairs(self):
        temp = self.head
        c = 0
        k = 6
        while temp.next!=None:
            temp1 = temp.next
            while temp1!=None:
                if temp.data + temp1.data <=k :
                    c+=1
                temp1=temp1.next
            temp=temp.next
        print(c)
    def print_second_half(self):
        temp = self.head
        i = 0
        while temp != None:
            i = i+1
            temp = temp.next
        j = 1
        temp1=self.head
        while temp1!=None:
            if j>i//2:
                print(temp1.data,j)
            j = j+1
            temp1=temp1.next
            
    def mid(self):
        f = self.head
        s = self.head
        while f!=None and f.next!=None: #if length is even remove .next and donot swap conditions
            f = f.next.next
            s= s.next
        print(s.data)
    def second_half(self):
        f = self.head
        s = self.head
        while f!=None and f.next!=None: 
            f = f.next.next
            s= s.next
        while s!=None:
            print(s.data,end="->")
            s=s.next
        print(None)
    def first_half(self):
        f=self.head
        s = self.head
        while f!=None and f.next!=None: 
            f = f.next.next
            print(s.data,end="->")
            s= s.next
        while s!=None:
            s=s.next
        print(None)
    def kth_node_fromlast(self):
        temp = self.head
        i = 0
        k = 3
        while temp != None:
            i = i+1
            temp = temp.next
        j = 1
        temp1=self.head
        while temp1!=None:
            if j==i-k:
                print(j)

            j = j+1
            temp1=temp1.next
    def kth_ele_last(self,k):
        f = self.head
        s = self.head
        for i in range(k):
            if f!=None: # if length is less than k value.
                f = f.next
        while f!=None:
            f= f.next
            s = s.next
        if s!=None:
            print(s.data)
    def kth_del(self,k):
        f = self.head
        s=self.head
        self.prev = None
        for i in range(k):
            f = f.next
        while f!=None:
            self.prev = s
            f=f.next
            s=s.next
        self.prev.next = s.next
    def swap_pairs(self):
        f = self.head
        f = f.next
        s=self.head
        while f!=None and f.next != None:
            s.data,f.data = f.data,s.data
            s=s.next.next
            f = f.next.next
        s.data,f.data = f.data,s.data
    def bubble_sort(self):
        temp = self.head
        while temp.next!=None:
            f= 0
            t = self.head
            while t.next != None:
                if t.data>t.next.data:
                    t.data,t.next.data = t.next.data,t.data
                    f = 1
                t=t.next
            temp = temp.next
            if f == 0:
                break

    def bubble_sort_using_kth_largest(self,k1):
        temp = self.head
        k=k1
        while temp.next!=None:
            f= 0
            t = self.head
            while t.next != None and k1!=0:
                if t.data>t.next.data:
                    t.data,t.next.data = t.next.data,t.data
                    f = 1
                t=t.next
            
            if f == 0:
                break
            k = k-1
            temp = temp.next
        self.kth_ele_last(k1)
    def check_loop(self):
        f = self.head
        s = self.head
        while f!=None and f.next!=None:
            f=f.next.next
            s = s.next
            if f == s:
                print("loop")
                return 
        print("no loops")
    def find_head(self):
        f = self.head
        s = self.head
        while f!=None and f.next!=None:
            f=f.next.next
            s = s.next
            if f == s:
                print("loop")
                break
        temp=self.head            
        while s!=temp:
            s = s.next
            temp = temp.next
        print( temp.data)
    def break_loop(self):
        f = self.head
        s = self.head
        prev = self.head
        temp = self.head
        while f.next!=None and f.next.next!=None:
            f=f.next.next
            s = s.next
            if f == s:
                break
        else:
            print("no loop")
            return                 
        while s!= temp:
            prev = s
            temp=temp.next
            s = s.next
        prev.next = None
    def count_node_inloop(self):
        f = self.head
        s = self.head
        prev = self.head
        temp = self.head
        while f.next!=None and f.next.next!=None:
            f=f.next.next
            s = s.next
            if f == s:
                break
        else:
            print("no loop")
        c = 1
        s=s.next
        while f != s:
            s = s.next
            c+=1
        print( c)
    def reverse_list(self):
        temp = self.head
        prev = None
        while temp :
            newnode = temp.next
            temp.next = prev
            prev = temp
            temp = newnode
        self.head = prev
    def reverse(self):
        prev = None
        c = self.head
        new_node=c.next
        while c != None:
            c.next = prev
            prev = c
            c = new_node
            if c == None:
                break
            new_node = c.next
        self.head = prev
    def reverse_second_half(self):
        f = self.head
        s = self.head
        while f != None and f.next != None:
            f = f.next.next
            pr = s
            s = s.next
        p = None   #for reverse
        c = s
        while c != None:
            n = c.next
            c.next = p
            p = c
            c = n
        pr.next = p
    def reverse_second_half_odd(self):
        f = self.head
        s = self.head
        while f != None and f.next != None:
            f = f.next.next
            pr = s
            s = s.next
        pr = s
        p = None   #for reverse
        c = s.next
        while c != None:
            n = c.next
            c.next = p
            p = c
            c = n
        pr.next = p
def intersection():
    t1=l1.head
    t2=l2.head
    while t1 != t2:
        if t1!= None:
            t1=t1.next
        else:
            t1 = l2.head
        if t2 != None:
            t2=t2.next
        else:
            t2 = l1.head
    print(t1.data,t2.data)
        
 
l1=linked()
l1.head = node(10)
l1.add_back(20)
l1.add_back(30)
l1.add_back(40)
l1.add_back(50)
l1.add_back(60)
l1.display()
#l1.sum_all()
#l1.sum_even()
#l1.sum_of_even_pos()
#l1.second_largest_num()
#l1.count_consecutive_pair()
#l1.count_possible_pairs()
#l1.print_second_half()
#l1.mid()
#l1.second_half()
#l1.first_half()
#l1.kth_node_fromlast()
#l1.kth_ele_last(8)
#l1.kth_del(3)
#l1.display()
#l1.swap_pairs()
#l1.display()
#l1.bubble_sort()
#l1.display()
#l1.bubble_sort_using_kth_largest(3)
#l1.check_loop()
reverse_second_half_odd = p
l2 = linked()
l2.head = node(100)
l2.head.next = node(200)
l2.head.next.next = node(300)
l2.head.next.next.next = node(400)
l2.head.next.next.next.next = node(500)
l2.head.next.next.next.next.next = p

#l2.check_loop()
#l2.find_head()
#l2.break_loop()
#l2.display()
#l2.count_node_inloop()
#l1.reverse_list()
#l1.display()
#l1.reverse()
#l1.display()
#l1.reverse_second_half()
#l1.reverse_second_half_odd()
#l1.display()
intersection()
#palindrome or nor
#merge sort using sll






