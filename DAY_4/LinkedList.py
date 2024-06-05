class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Sll:
    def __init__(self):
        self.head = None

    def display(self):
        t = self.head
        while t is not None:
            print(t.data, end="->")
            t = t.next
        print("None")

    def addback(self, x):
        new_node = Node(x)
        if self.head is None:
            self.head = new_node
            return
        t = self.head
        while t.next is not None:
            t = t.next
        t.next = new_node

    def addeven(self):
        t = self.head
        s = 0
        while t is not None:
            if t.data % 2 == 0:
                s += t.data
            t = t.next
        return s

    def addfront(self, x):
        new_node = Node(x)
        new_node.next = self.head
        self.head = new_node

    def search(self, x):
        t = self.head
        while t is not None:
            if t.data == x:
                print("Found")
                return
            t = t.next
        print("Not Found")

    def middlenode(self):
        # length=1
        # t=self.head
        # while t.next!=None:
        #     length+=1
        #     t=t.next
        # f=self.head

        # print("length",length)
        # if length%2==0:
        #     for i in range((length//2)):
        #         f=f.next
        #     print(f.data)
        # if length%2!=0:
        #     for i in range((length//2)):
        #         f=f.next
        #     print(f.data)
        f = self.head
        s = self.head
        while(f!=None and f.next!=None):
            s=s.next
            f=f.next.next
        print(s.data)

    def lengthlinkedlist(self):
        fc=1
        f=self.head
        while( f!=None and f.next!=None):
            f=f.next.next
            fc+=2
        if f==None:
            print("Even")
        else:
            print("Odd")
        print(fc)











a = Sll()
a.head=Node(10)
a.addback(20)
a.addback(40)
a.addback(50)
a.addback(60)
# a.addback(70)
a.addback(80)
a.display()
a.middlenode()
a.display()
# a.search(20)
# a.search(40)
# a.middlenode()
a.lengthlinkedlist()
