class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Sll:
    def __init__(self):
        self.head = None

    def display(self):
        print("---------START------------")
        t = self.head
        while t is not None:
            print(f"{t.data}-{t}\n")
            # print(t.data, end="->")
            t = t.next
        print("None")
        print("-----------END------------")

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


    def delete(self):
        n=int(input("\nenter node to delete :"))
        t=self.head
        prev=None
        while(t!=None and t.next!=None):
            if t.data==n:
                if prev:
                    prev.next=t.next
                else:
                    self.head=t.next
                t=t.next
            else:
                prev=t
                t=t.next
            # if t.next.data==n:
            #     print("A t.next",t.next)
            #     t.next=t.next.next
            #     print("C",t.next)
            #     t=t.next
            #     print("t",t)
            # elif self.head.data==n:
            #     print("self.head.data",self.head.data)
            #     print("self.head",self.head)
            #     self.head=self.head.next
            #     print("self.head.next",self.head.next)
            #     print("self.head",self.head)
            #     t=self.head
            # else:
            #     t=t.next


            # if t.data==n:
            #     if t==self.head:
            #         print("A ",t.data)
            #         print("head b",self.head)
            #         print("t.next",t.next)
            #         self.head=t.next
            #         t=self.head
            #         print("head a",self.head)
            #         print("t",t)
            #         # t = t.next
            # # if t.next.data==n:
            # #     if t == self.head:
            # #         print("B ",t.data)
            # #         self.head = t.next
            # #         t.next=t.next.next
            # #         t=t.next
            # t=t.next












a = Sll()
a.head=Node(7)
a.addback(7)
a.addback(7)
a.addback(7)
# a.addback(60)
# # a.addback(70)
# a.addback(80)

# a.middlenode()
# a.display()
# a.search(20)
# a.search(40)
# a.middlenode()
# a.lengthlinkedlist()
# a.addback(2)
# a.addback(6)
# a.addback(3)
# a.addback(4)
# a.addback(5)
# a.addback(6)
a.display()
a.delete()
a.display()

