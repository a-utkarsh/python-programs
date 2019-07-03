class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None

    def insertBeg(self,item):
        newNode=Node(item)
        newNode.next=self.head
        self.head=newNode

    def insertLast(self,item):
        temp=self.head
        while temp.next!=None:
            temp=temp.next
        newnode=Node(item)
        newnode.next=None
        temp.next=newnode

    def insertMiddle(self,item,key):
        temp=self.head
        while temp.data!=key:
            temp=temp.next
        newNode=Node(item)
        newNode.next=temp.next
        temp.next=newNode

    def deletemiddle(self,item):
        #item = self.middle2()
        temp = self.head
        while temp.next.data != item:
            temp = temp.next
        #temp1 = temp.next
        temp.next = temp.next.next
        #del (temp1)  # to free the space
    def deletefirst(self):
        temp=self.head
        temp1=self.head.next
        self.head=temp1
        del(temp)

    def deleteLast(self):
        temp=self.head
        while(temp.next.next!=None):
            temp=temp.next
        temp.next=None

    def printllist(self):
        temp = self.head
        while temp:
            print(temp.data, end="=>")
            temp = temp.next
        print("Null")


llist=LinkedList()
llist.insertBeg(4)
llist.insertBeg(3)
llist.insertBeg(2)
llist.insertBeg(1)
llist.printllist()
llist.insertMiddle(6,3)
llist.printllist()
llist.insertLast(5)
llist.printllist()
llist.deletefirst()
llist.printllist()
llist.deleteLast()
llist.printllist()
