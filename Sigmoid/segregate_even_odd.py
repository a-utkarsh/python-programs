class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:

    def __init__(self):
        self.head=None

    def insertBeg(self,key):
        newNode=Node(key)
        newNode.next=self.head
        self.head=newNode
    def segregateEvenOdd(self):
        evenStart=None
        evenEnd=None
        oddStart=None
        oddEnd=None

        currNode=self.head

        while currNode!=None:
            if currNode.data%2==0:
                if evenStart==None:
                    evenStart=currNode
                    evenEnd=evenStart
                else:
                    evenEnd.next=currNode
                    evenEnd=evenEnd.next
            else:
                if oddStart==None:
                    oddStart=currNode
                    oddEnd=oddStart
                else:
                    oddEnd.next=currNode
                    oddEnd=oddEnd.next
            currNode=currNode.next
        if evenStart is None or oddStart is None:
            return

        oddEnd.next = evenStart
        evenEnd.next = None

        self.head = oddStart

    def printList(self):
        temp=self.head
        while temp:
            print(temp.data,end="->")
            temp=temp.next
        print("Null")


llist = LinkedList()
llist.insertBeg(11)
llist.insertBeg(10)
llist.insertBeg(9)
llist.insertBeg(6)
llist.insertBeg(4)
llist.insertBeg(1)
llist.insertBeg(0)
print("Before Rearrange")
llist.printList()
llist.segregateEvenOdd()
print("After Rearrange")
llist.printList()


