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

    def copy(self):
        temp=self.head
        copylist=None
        while temp:
            copylist=temp
            temp=temp.next
        return copylist

    def printllist(self):
        temp = self.head
        while temp:
            print(temp.data, end="=>")
            temp = temp.next
        print("Null")

llist=LinkedList()

llist.insertBeg(5)
llist.insertBeg(4)
llist.insertBeg(3)
llist.insertBeg(2)
llist.insertBeg(1)
llist.printllist()

llist.printllist()