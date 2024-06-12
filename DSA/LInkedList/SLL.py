class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class sll:
    def __init__(self):
        self.head=None

    def addfront(self,x):
        newnode=Node(x)
        newnode.next=self.head
        self.head=newnode

    def display(self):
        t=self.head
        while(t!=None):
            print(t.data,end="->")
            t=t.next
        print(None)


    def addback(self,x):
        newnode=Node(x)
        t=self.head
        while t.next!=None:
            t=t.next
        t.next=newnode
        newnode.next=None

    def delete(self):
        key=int(input("Enter the key to delete: "))
        t=self.head
        p=None
        while t!=None and t.data==key:
            self.head=t.next
            t=self.head
            print("A")

        # t = self.head
        while t!=None:
            if t.data==key:
                print("B")
                p.next=t.next
                t=p.next
            else:
                print("C")
                p=t
                t=t.next


    def reverse(self):



obj=sll()
obj.addfront(1)
obj.display()
obj.addback(2)
obj.addback(6)
obj.addback(3)
obj.addback(4)
obj.addback(5)
obj.addback(6)
obj.display()
# obj.delete()
obj.reverse()
obj.display()

