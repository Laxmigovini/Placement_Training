class node:
    def __init__(self,data):
        self.data = data
        self.next = None
class linked:
    def __init(self):
        self.head = head
    def add_ele(self,data):
        temp = self.head
        while temp.next != None:
            temp = temp.next
        temp.next = node(data)
    def display(self):
        temp = self.head
        while temp != None:
            print(temp.data,end = "->")
            temp = temp.next
        print("None")
    def summ(self):
        temp = self.head
        s = 0
        while temp != None:
            s += temp.data
            temp = temp.next
        print(s)
    def sum_even(self):
        temp = self.head
        s = 0
        while temp != None:
            if temp.data % 2 == 0:
                s += temp.data
            temp = temp.next
        print(s)
    def even_pos_sum(self):
        temp = self.head
        pos = 1 
        s = 0
        while temp.next != None:
            if pos % 2 == 0:
                s+= temp.data
            pos += 1
            temp = temp.next
        print(s)
    def second_largest(self):
        temp = self.head
        max1 = -9999
        max2 = -9999
        while temp.next != None:
            if max1 < temp.data:
                max2 = max1
                max1 = temp.data
            if temp.data>max2 and temp.data != max1:
                max2 = temp.data
            temp = temp.next
        print(max2)
    def count_consecutive_pair(self):
        temp = self.head
        s = 0
        k = 5
        c=0
        while temp.next != None:
            s=temp.data + temp.next.data
            if s <= k:
                c+=1
            temp = temp.next
        print(c)
    def count_possible_pairs(self):
        temp = self.head
        s=0
        k = 7
        c= 0
        while temp.next != None:
            temp1 = temp.next
            while temp1 != None:
                if temp1.data+temp.data <=k:
                    c+=1
                temp1=temp1.next
            temp=temp.next
        print(c)
    def second_half(self):
        temp = self.head
        i = 0
        while temp != None:
            i = i+1
            temp = temp.next
        temp1 = self.head
        j = 1
        while temp1 != None:
            if j>i//2:
                print(temp1.data,end="->")
            j+=1
            temp1 = temp1.next
    def mid(self):
        f = self.head
        s = self.head
        while f != None and f.next != None:
            f= f.next.next
            s = s.next
        print(s.data)
    def secnd_half(self):
        f=self.head
        s=self.head
        while f != None and f.next != None:
            f = f.next.next
            s = s.next
        while s != None:
            print(s.data,end="->")
            s=s.next
    def kth_node_fromlast(self):
        temp= self.head
        i = 0
        k = 3
        while temp != None:
            i = i+1
            temp = temp.next
        temp1=self.head
        j = 1
        while temp1 != None:
            if j==i-k:
                print(j)
            j+=1
            temp1 = temp1.next
                

l1 = linked()
l1.head = node(6)
l1.add_ele(1)
l1.add_ele(2)
l1.add_ele(3)
l1.add_ele(4)
l1.add_ele(5)
l1.add_ele(6)
l1.display()
#l1.summ()
#l1.sum_even()
#l1.even_pos_sum()
#l1.second_largest()
#l1.count_consecutive_pair()
#l1.count_possible_pairs()
#l1.second_half()
#l1.mid()
#l1.secnd_half()
l1.kth_node_fromlast()
