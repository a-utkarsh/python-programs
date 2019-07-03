class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None

class DoubleLinkedList:
    def __init__(self):
        self.head=None

    def insertbeg(self,item):
        newNode=Node(item)
        newNode.next=self.head
        newNode.prev=None
        # 4. change prev of head node to new_node
        if self.head is not None:
            self.head.prev=newNode
        self.head=newNode

    def insertafter(self,key,item):
        temp=self.head
        while temp.data!=key:
            temp=temp.next
        newNode=Node(item)
        newNode.next=temp.next
        temp.next=newNode
        newNode.prev=temp

        if newNode.next is not None:
            newNode.next.prev=newNode

    def insertLast(self,item):
        newNode=Node(item)
        newNode.next=None
        temp=self.head
        while temp.next is not None:
            temp =temp.next
        temp.next=newNode
        newNode.prev=temp
        return

    def printlist(self):
        temp=self.head
        while temp:
            print(temp.data,end="=>")
            temp=temp.next

        print("Null")


dll=DoubleLinkedList()
dll.insertbeg(5)
dll.insertbeg(4)
dll.insertbeg(3)
dll.insertbeg(2)
dll.insertbeg(1)
dll.insertLast(6)
dll.insertLast(7)
dll.insertLast(8)
dll.insertafter(5,10)
dll.printlist()

