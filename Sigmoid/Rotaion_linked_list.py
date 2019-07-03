class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None

    def insertbeg(self,item):
        newnode=Node(item)
        newnode.next=self.head
        self.head=newnode

    def rotation(self,k):
        count=1
        temp=self.head
        while(count!=k):
            temp=temp.next
            count+=1
        kth = temp
        while temp.next!=None:
            temp=temp.next
        temp.next=self.head
        self.head=kth.next
        kth.next=None
    def printllist(self):
        temp = self.head
        while temp:
            print(temp.data, end="=>")
            temp = temp.next
        print("Null")
llist=LinkedList()
llist.insertbeg(60)
llist.insertbeg(50)
llist.insertbeg(40)
llist.insertbeg(30)
llist.insertbeg(20)
llist.insertbeg(10)
llist.printllist()
llist.rotation(4)
llist.printllist()
