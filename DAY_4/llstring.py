class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class sll:

    def __init__(self):
        self.head=None

    def add_front(self,data):
        newnode=Node(data)
        newnode.next=self.head
        self.head=newnode

    def display(self):
        temp=self.head
        while (temp!=None):
            print(temp.data,end="->")
            temp=temp.next
        print(None)

    def longest_sub_string(self):
        c=1
        m=1
        temp=self.head
        while (temp.next!=None):
            if (temp.data==temp.next.data-1):
                c=c+1
            else:
                if(c>m):
                    m=c
            temp=temp.next
        if (c>m):
            m=c
        print(m)

    def sorting(self):
        s=self.head
        while(s!=None and s.next!=None):
            f=s.next
            while(f!=None and f.next!=None):
                if f.data>s.data:
                    s.data,f.data=f.data,s.data

                    f = f.next
                f=f.next
            s=s.next



    def print_pairs(self):
        s=self.head
        # s=s.next.next
        while (s!=None and s.next!=None):
            f = s.next
            while(f!=None and f.next!=None):
                print(f"{s.data}{f.data}")
                f=f.next
            s = s.next

obj=sll()
obj.add_front(1)
obj.add_front(0)
obj.add_front(2)
obj.add_front(4)
obj.add_front(8)
obj.add_front(4)
obj.add_front(7)
obj.add_front(6)
obj.display()
# obj.longest_sub_string()
# obj.print_pairs()
obj.sorting()
obj.display()
