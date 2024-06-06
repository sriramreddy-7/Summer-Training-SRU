class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class dll:
    def __init__(self):
        self.head=None
        self.tail=None

    def addback(self,x):
        if self.head==None:
            self.head=Node(x)
            self.tail=self.head
        else:
            t=Node(x)
            self.tail.next=t
            t.prev=self.tail
            self.tail=self.tail.next


    def addfront(self,x):
        if self.head == None:
            self.head = Node(x)
            self.tail = self.head
        else:
            t=Node(x)
            self.head.prev=t
            t.next=self.head
            self.head=self.head.prev

    def display(self):
        t=self.head
        while(t!=None):
            print(t.data,end="->")
            t=t.next
        print(None)

    def reverse(self):
        t=self.tail
        while(t!=None):
            print(t.data,end="->")
            t=t.prev

    def search(self):
        x=int(input("\nEnter element: "))
        f=self.head
        b=self.tail
        count=0
        while(f!=b and f!=b.next):
            if f.data==x or b.data==x:
                return 1
            f=f.next
            b=b.prev
        if f.data==x:
            return 1
        return 0

    def length(self):
        f=self.head
        b=self.tail
        while(f!=b and f!=b.next):
            f=f.next
            b=b.prev
            # print("\n",1)
        if f!=b:
            return "even"
        return "odd"

    def palindrome(self):
        f=self.head
        b=self.tail
        while(f!=b and f!=b.next):
            if f.data==b.data:
                f=f.next
                b=b.prev
            else:
                return "not plaindrome"
        if f.data ==b.data or f.data ==d.next.data:
            return "Palindrome"



a = dll()
a.addback(20)
a.addback(40)
a.addback(50)
a.addback(60)
# a.addback(70)
a.addback(80)
a.addfront(10)
a.addfront(1)
a.display()
a.reverse()
# print(a.search())
print(a.length())
print(a.palindrome())






